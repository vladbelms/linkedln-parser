from blessed import Terminal


class Menu:
    def show_base_info(self, project_name: str) -> None:
        term = Terminal()
        with term.fullscreen(), term.cbreak():
            print(term.home + term.clear)
            print(f"{term.bold}it's a {project_name}{term.normal}")
            print("\n\n" + term.italic + "Press any key to exit..." + term.no_italic)
            term.inkey()

    def get_menu_data(self, promt: str) -> int:
        term = Terminal()
        print(term.clear)
        with term.cbreak():
            promt = str(promt)
            print(term.move_y(term.height // 2) + term.center(promt), end='', flush=True)

            number = ''
            while True:
                key = term.inkey()
                if key.isdigit():
                    number += key
                    print(key, end='', flush=True)
                elif key.code == term.KEY_ENTER:
                    break
        return int(number)

    def show_list(self, list_: list) -> None:

        term = Terminal()
        with term.fullscreen(), term.cbreak():
            print(term.clear)
            print(term.move_y(term.height // 2 - len(list_) // 2))

            for dictionary in list_:
                for key, value in dictionary.items():
                    print(f"{key}: {value}")
                print(term.horizontal_line(term.width))

            print(term.move(term.height - 1, 0) + "Press any key to exit...")
            term.inkey()
