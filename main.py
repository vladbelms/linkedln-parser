from linkedln_parser import Linkedln


def main():
    url = Linkedln([""], ["USA"])
    print(url.get_data(5))


if __name__ == '__main__':
    main()
