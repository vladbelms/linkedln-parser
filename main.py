from src import Menu, LinkedIn


def region_handler(current_value, key_event):
    regions = ['UK', 'USA', 'EU']
    current_index = regions.index(current_value)
    if key_event == 'KEY_LEFT':
        current_index = (current_index - 1) % len(regions)
    elif key_event == 'KEY_RIGHT':
        current_index = (current_index + 1) % len(regions)
    return regions[current_index]


def vacancies_handler(current_value, key_event):
    if key_event == 'KEY_LEFT':
        return max(1, current_value - 1)
    elif key_event == 'KEY_RIGHT':
        return current_value + 1
    return current_value


def main():
    settings = {
        "Region": "USA",
        "Vacancies": 5
    }

    setting_handlers = {
        "Region": region_handler,
        "Vacancies": vacancies_handler
    }

    menu = Menu(
        title="Generic Application",
        options=["Start", "Settings", "Exit"],
        settings=settings,
        setting_handlers=setting_handlers
    )
    while True:
        selected_option = menu.display_menu()
        if selected_option == 2:
            break
        elif selected_option == 1:
            menu.settings_menu()
        elif selected_option == 0:
            region = menu.settings["Region"]
            vacancies = menu.settings["Vacancies"]
            linkedin = LinkedIn([""],[region])
            list_ = linkedin.get_data(vacancies)
            menu.show_list(list_, title="Vacancies List")


if __name__ == '__main__':
    main()
