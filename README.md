# easyfont


**One line of code, your ideal font is ready — EasyFont.**



**Install**

```bash
pip install easyfont
```


**Usage**


```python
import easyfont
from easyfont import Lang, FontConfig
from easyfont import getfont


def main():
    print("Hello from easyfont!")
    print(easyfont.__version__)
    print(getfont()) # default font
    print(easyfont.getfont(lang=Lang.EN_US))  # one language
    print(getfont(lang=[Lang.EN_US, Lang.ZH_TW]))  # multiple languages

    cfg = FontConfig(lang=[Lang.EN_US, Lang.ZH_CN, Lang.ZH_TW])  # use FontConfig
    print(getfont(cfg=cfg))  # use FontConfig with multiple languages


if __name__ == "__main__":
    main()

```