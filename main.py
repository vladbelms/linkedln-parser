from linkedln_parser import Linkedln


def main():
    url = Linkedln(["ml"], ["USA"])
    url.parse_name_companies()
    url.parse_country_companies()
    print(url.return_list())


if __name__ == '__main__':
    main()
