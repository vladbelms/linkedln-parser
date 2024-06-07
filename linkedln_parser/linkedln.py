import httpx
from bs4 import BeautifulSoup


class Linkedln:
    def __init__(self, description: list[str], location: list[str]) -> None:
        self.__description = description
        self.__location = location
        self.my_dict: dict[str, str] = {}
        self.my_list: list[dict[str, str]] = []

    @property
    def description(self):
        return self.__description

    @property
    def location(self):
        return self.__location

    def save_link(self) -> str:
        link = f"https://www.linkedin.com/jobs/search?keywords={'%20'.join(self.__description)}&location={'%20'.join(self.__location)}trk=guest_homepage-basic_guest_nav_menu_jobs"
        return link

    def add_dict_values(self, key: str, value: str) -> None:
        self.my_dict[key] = value

    def parse_html(self) -> BeautifulSoup:
        link = self.save_link()
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        return results

    def parse_name_companies(self) -> None:
        results = self.parse_html()
        name_companies = results.find_all("h3", class_="base-search-card__title")
        for company in name_companies:
            self.add_dict_values("job title", company.get_text(strip=True))
            self.my_list.append(self.my_dict)

    def parse_country_companies(self) -> None:
        results = self.parse_html()
        country_companies = results.find_all("h4", class_="base-search-card__subtitle")
        for name_company in country_companies:
            self.add_dict_values("name company", name_company.get_text(strip=True))
            self.my_list.append(self.my_dict)

    def return_list(self) -> list[dict[str: str]]:
        return self.my_list
