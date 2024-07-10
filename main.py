from src import Menu, Linkedln


def main():
    menu = Menu()
    region = menu.region
    vacancies = menu.vacancies
    url = Linkedln([""], [region])
    list_ = url.get_linkedln_data(vacancies)
    menu.all_data(list_)

if __name__ == '__main__':
    main()
