from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

try:
    from importlib.resources import files
except ImportError:
    # for Python < 3.9
    from importlib_resources import files

from typing import Optional, Union, Iterable


class Lang(Enum):
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"
    EN_US = "en_US"


class FontName(Enum):
    NOTO_SANS_SC = "NotoSansSC"
    NOTO_SANS_TC = "NotoSansTC"
    NOTO_SANS = "NotoSans"


@dataclass
class FontConfig:
    lang: Optional[Union[Lang, Iterable[Lang]]] = field(default=None)
    name: FontName = field(default=None)

    def __post_init__(self):
        self.lang = set(self.lang) if isinstance(self.lang, Iterable) else {self.lang} if self.lang else set()


@dataclass
class Font(FontConfig):
    file_name: Optional[str] = field(default=None)

    @property
    def path(self):
        file_path = Path(str(files("easyfont.fonts").joinpath(self.file_name)))
        if not file_path.exists():
            raise FileNotFoundError(f"Font file {self.name.value} not found in easyfont fonts directory.")
        return file_path




NOTO_SANS_SC = Font(name=FontName.NOTO_SANS_SC, lang=[Lang.ZH_CN, Lang.EN_US], file_name="NotoSansSC-Regular.ttf")
NOTO_SANS_TC = Font(name=FontName.NOTO_SANS_TC, lang=[Lang.ZH_TW, Lang.EN_US], file_name="NotoSansTC-Regular.ttf")
NOTO_SANS = Font(name=FontName.NOTO_SANS, lang=[Lang.EN_US], file_name="NotoSans-Regular.ttf")
DEFAULT_FONT = NOTO_SANS_SC



_FONT_LIBRARY = {
    NOTO_SANS_SC.name: NOTO_SANS_SC,
    NOTO_SANS_TC.name: NOTO_SANS_TC,
    NOTO_SANS.name: NOTO_SANS
}

_FONT_LANG_SUPPORT = {
    NOTO_SANS.name: NOTO_SANS.lang,
    NOTO_SANS_SC.name: NOTO_SANS_SC.lang,
    NOTO_SANS_TC.name: NOTO_SANS_TC.lang
}
