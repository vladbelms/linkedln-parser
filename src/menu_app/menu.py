from blessed import Terminal


class Menu:
    @staticmethod
    def present(project_name):
        term = Terminal()
        with term.fullscreen(), term.cbreak():
            print(term.home + term.clear)
            print(f"{term.bold}it's a {project_name}{term.normal}")
            print("\n\n" + term.italic + "Press any key to exit..." + term.no_italic)
            term.inkey()

    @staticmethod
    def get_data(promt : str) -> int:
        term = Terminal()
        print(term.clear)
        with term.cbreak():
            prompt = str(promt)
            print(term.move_y(term.height // 2) + term.center(prompt))

            number = ''
            while True:
                key = term.inkey()
                if key.isdigit():
                    number += key
                    print(term.move_yx(term.height // 2, (term.width // 2 - len(prompt) // 2) + len(prompt)) + number)
                elif key.code == term.KEY_ENTER:
                    break
        return int(number)

    @staticmethod
    def get_list(list_: list) -> None:

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
