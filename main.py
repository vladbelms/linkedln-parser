from src import Menu, LinkedIn


def main():
    menu = Menu()
    region = menu.region
    vacancies = menu.vacancies
    linkedin = LinkedIn([""], [region])
    list_ = linkedin.get_data(vacancies)
    menu.display_menu(list_, linkedin)

if __name__ == '__main__':
    main()
