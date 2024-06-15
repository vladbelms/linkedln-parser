from typing import Any

import httpx
from bs4 import BeautifulSoup


class Linkedln:
    def __init__(self, keywords: list[str], location: list[str]) -> None:
        self.__keywords = keywords
        self.__location = location

    @property
    def description(self):
        return self.__keywords

    @property
    def location(self):
        return self.__location

    def get_data(self, count: int = 20) -> list[dict[str, Any]]:
        link = f"https://www.linkedin.com/jobs/search?keywords={'%20'.join(self.__keywords)}&location={'%20'.join(self.__location)}trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0"
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        parse_list = []
        job_titles = results.find_all("h3", class_="base-search-card__title")
        country_companies = results.find_all("h4", class_="base-search-card__subtitle")
        job_titles = job_titles[:count]
        country_companies = country_companies[:count]
        for job_title, name_company in zip(job_titles, country_companies):
            parse_list.append({
                "job title": job_title.get_text(strip=True),
                "name company": name_company.get_text(strip=True)
            })
        return parse_list
