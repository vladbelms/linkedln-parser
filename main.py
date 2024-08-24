from src import KeyMode , Option , LinkedIn, NumberAdjuster, ListSelector


def adjust_number():
    adjuster = NumberAdjuster(start_number=5)
    final_number = adjuster.adjust()
    print(f"Final number: {final_number}")
    return final_number

def choose_country():
    countries = ["USA", "UK", "EU"]
    selector = ListSelector(items=countries)
    selected_country = selector.select()
    print(f"Selected country: {selected_country}")
    return selected_country



def main():
    def show_main_menu():
        key_mode = KeyMode(options=main_menu_options, description="Select an option:")
        key_mode()

    def show_settings_menu():
        key_mode = KeyMode(options=settings_menu_options, description="Settings:")
        key_mode()

    def get_linkedin():
        return LinkedIn([""], [choose_country()])

    def parsing_data_handler():
        linkedin = get_linkedin()
        data = linkedin.get_data(adjust_number())
        for i in range(0, adjust_number()):
            dictionary = data[i]
            for key, value in dictionary.items():
                print(f"{key}: {value}")

    main_menu_options = [
        Option(
            name="Parsing data",
            handler= parsing_data_handler
        ),
        Option(
            name="Settings",
            handler=show_settings_menu
        ),
    ]
    settings_menu_options = [
        Option(
            name="Country",
            handler= choose_country
        ),
        Option(
            name="Vacancies",
            handler=adjust_number
        ),
        Option(
            name="Exit",
            handler= show_main_menu
        )
    ]

    show_main_menu()


if __name__ == '__main__':
    main()
