from src import Menu, Linkedln


def main():
    menu = Menu()
    menu.show_base_info("Linkedln Parser")
    number = menu.get_menu_data("Print a positive number")
    url = Linkedln([""], ["USA"])
    list_ = url.get_linkedln_data(number)
    menu.show_list(list_)


if __name__ == '__main__':
    main()
