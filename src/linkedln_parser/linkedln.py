from typing import Any

import httpx
from bs4 import BeautifulSoup


class Linkedln:
    def __init__(self, keywords: list[str], location: list[str]) -> None:
        self.__keywords = keywords
        self.__location = location

    @property
    def keywords(self):
        return self.__keywords

    @property
    def location(self):
        return self.__location

    def get_linkedln_data(self, count: int = 20) -> list[dict[str, Any]]:
        link = f"https://www.linkedin.com/jobs/search?keywords={'%20'.join(self.__keywords)}&location={'%20'.join(self.__location)}trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0"
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        list_ = []
        job_titles = results.find_all("h3", class_="base-search-card__title")
        company_contries = results.find_all("h4", class_="base-search-card__subtitle")
        datetimes = results.find_all("time", class_="job-search-card__listdate")
        job_titles = job_titles[:count]
        company_contries = company_contries[:count]
        datetimes = datetimes[:count]
        for job_title, name_company, date in zip(job_titles, company_contries, datetimes):
            list_.append({
                "job_title": job_title.get_text(strip=True),
                "name_company": name_company.get_text(strip=True),
                "datetime": date['datetime']
            })
        return list_
