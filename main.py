from src import Menu, LinkedIn


def main():
    menu = Menu()
    region = menu.region
    vacancies = menu.vacancies
    url = LinkedIn([""], [region])
    list_ = url.get_linkedin_data(vacancies)
    menu.all_data(list_)

if __name__ == '__main__':
    main()
