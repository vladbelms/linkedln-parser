from linkedln_parser import Linkedln


def main():
    url = Linkedln("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
    url.get_name()


if __name__ == '__main__':
    main()