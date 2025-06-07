import easyfont
from easyfont import Lang, FontConfig
from easyfont import getfont


def main():
    print("Hello from easyfont!")
    print(easyfont.__version__)
    print(getfont())
    print(easyfont.getfont(lang=Lang.EN_US))
    print(getfont(lang=[Lang.EN_US, Lang.ZH_TW]))
    print(getfont(lang=[Lang.EN_US, Lang.ZH_CN, Lang.ZH_TW]))

    cfg = FontConfig(lang=Lang.EN_US)
    print(getfont(cfg=cfg))


if __name__ == "__main__":
    main()
