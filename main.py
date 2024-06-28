from src import Menu, Linkedln


def main():
    Menu.present("Linkedln Parser")
    number = Menu.get_data("Print a positive number")
    url = Linkedln([""], ["USA"])
    list_ = url.get_data(number)
    Menu.get_list(list_)


if __name__ == '__main__':
    main()
