import warnings
from functools import lru_cache

from ._types import Lang, Font, _FONT_LANG_SUPPORT, FontName, FontConfig, DEFAULT_FONT, _FONT_LIBRARY

try:
    from importlib.resources import files
except ImportError:
    # for Python < 3.9
    from importlib_resources import files

from typing import Union, Iterable, Tuple


@lru_cache(maxsize=None)
def _search_font_cached(lang_tuple: Tuple[Lang, ...], fallback: bool) -> Font:
    lang_set = set(lang_tuple)

    best_match = None
    best_score = -1

    for font_name, supported_langs in _FONT_LANG_SUPPORT.items():
        match_score = len(lang_set & supported_langs)
        if match_score > best_score:
            best_match = font_name
            best_score = match_score

    if best_match and best_score > 0:
        return _FONT_LIBRARY[best_match]

    if fallback:
        return DEFAULT_FONT

    raise ValueError(f"No font found for languages: {lang_set}")


def search_font(lang: Union[Lang, Iterable[Lang]], fallback: bool = True) -> Font:
    if isinstance(lang, Lang):
        lang_tuple = (lang,)
    else:
        lang_tuple = tuple(lang)

    return _search_font_cached(lang_tuple, fallback)


def load_font(cfg: FontConfig, fallback: bool = True) -> Font:
    lang = cfg.lang
    name = cfg.name

    if isinstance(name, FontName) or name in FontName._value2member_map_:
        return _FONT_LIBRARY[name]
    else:
        if lang:
            return search_font(lang=lang, fallback=fallback)
        else:
            if fallback:
                return DEFAULT_FONT
            else:
                raise ValueError("No font name or language provided, and fallback is disabled.")


def get_font(cfg: FontConfig = None, as_obj: bool = False, fallback: bool = True, **kwargs) -> Union[str, Font]:
    if cfg is not None and kwargs:
        warnings.warn("Both cfg and kwargs provided; kwargs will be ignored.", UserWarning)

    cfg = cfg or FontConfig(**kwargs)  # Ensure cfg is initialized if kwargs are provided

    try:
        font = load_font(cfg=cfg, fallback=fallback)
    except ValueError as e:
        if fallback:
            font = DEFAULT_FONT
            warnings.warn(f"Using default font due to error: {e}", UserWarning)
        else:
            raise e
    return font if as_obj else font.path
