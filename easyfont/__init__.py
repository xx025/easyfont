from ._core import getfont
from ._types import FontConfig, Lang

get_font = getfont

__all__ = [
    "getfont",
    "get_font",
    "FontConfig",
    "Lang",

]


from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("easyfont")
except PackageNotFoundError:
    __version__ = "unknown"