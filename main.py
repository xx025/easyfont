from easyfont.types import Lang


def main():
    print("Hello from easyfont!")

    from easyfont import get_font
    print(get_font())
    print(get_font(lang=[Lang.EN_US]))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_TW]))
    print(get_font(lang=[Lang.EN_US, Lang.ZH_CN]))


if __name__ == "__main__":
    main()
