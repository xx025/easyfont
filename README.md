
# easyfont


A simple font library for Python, designed to make working with fonts easy and intuitive.



Usage

```python
from easyfont.types import Lang


def main():
    from easyfont import get_font
    print(get_font())
    print(get_font(lang=[Lang.EN_US]))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_TW]))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_CN]))


if __name__ == "__main__":
    main()
    
```