from .menu_app import KeyMode, Option, Slider
from .linkedln_parser import LinkedIn


class App:
    def __init__(self):

        self.selected_country = ""

        self.main_menu_options = [
            Option(
                name="Parsing data",
                handler=self.parsing_data_handler
            ),
            Option(
                name="Settings",
                handler=self.show_settings_menu
            )
        ]
        self.settings_menu_options = [
            Option(
                name="Country",
                handler=self.country_selector_menu
            ),
            Option(
                name="Vacancies",
                handler=self.slider
            ),
            Option(
                name="Exit",
                handler=self.show_main_menu
            )
        ]
        self.country_selector_options = [
            Option(
                name="USA",
                handler=lambda: "USA"
            ),
            Option(
                name="UK",
                handler=lambda: "UK"
            ),
            Option(
                name="EU",
                handler=lambda: "EU"
            ),
            Option(
                name="Exit",
                handler=self.show_main_menu
            )
        ]

    def slider(self):
        def slider_handler(value):
            print(f"Slider value confirmed: {value}")

        slider = Slider(start_number=5, handler=slider_handler)
        return slider.activate()

    def show_main_menu(self):
        key_mode = KeyMode(elements=self.main_menu_options, description="Select an option:")
        key_mode()

    def show_settings_menu(self):
        key_mode = KeyMode(elements=self.settings_menu_options, description="Settings:")
        key_mode()

    def country_selector_menu(self):
        key_mode = KeyMode(elements=self.country_selector_options, description="Country:")
        selected_country = key_mode()

    def get_linkedin(self):
        return LinkedIn([""], [self.selected_country])

    def parsing_data_handler(self):
        linkedin = self.get_linkedin()
        number_of_vacancies = self.slider()
        data = linkedin.get_data(number_of_vacancies)
        for i in range(min(number_of_vacancies, len(data))):
            dictionary = data[i]
            for key, value in dictionary.items():
                print(f"{key}: {value}")

    def run(self):
        self.show_main_menu()
