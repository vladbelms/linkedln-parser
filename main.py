from src import Menu, Linkedln


def main():
    number = Menu.get_positive_number()
    url = Linkedln([""], ["USA"])
    list_ = url.get_data(number)
    Menu.get_list(list_)


if __name__ == '__main__':
    main()
