from src import Menu, LinkedIn


def main():
    menu = Menu()
    while True:
        menu.display_menu()
        if menu.should_exit:
            break
        region = menu.region
        vacancies = menu.vacancies
        linkedin = LinkedIn([""], [region])
        list_ = linkedin.get_data(vacancies)
        menu.show_list(list_)

if __name__ == '__main__':
    main()
