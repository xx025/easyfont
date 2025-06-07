# easyfont


**One line of code, your ideal font is ready — EasyFont.**



**Install**

```bash
pip install easyfont
```


**Usage**


```python
from easyfont import Lang, FontConfig
from easyfont import get_font


def main():
    print("Hello from easyfont!")

    print(get_font())
    print(get_font(lang=Lang.EN_US))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_TW]))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_CN, Lang.ZH_TW]))

    cfg= FontConfig(lang=Lang.EN_US)
    print(get_font(cfg=cfg))


if __name__ == "__main__":
    main()

```