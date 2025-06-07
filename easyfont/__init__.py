from ._core import getfont
from ._types import FontConfig, Lang

get_font = getfont

__all__ = [
    "getfont",
    "get_font",
    "FontConfig",
    "Lang",

]


def __version__():
    return "0.0.1-5"
