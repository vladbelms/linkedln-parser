from typing import Any
import datetime
import httpx
from bs4 import BeautifulSoup


class LinkedIn:
    def __init__(self, keywords: list[str], location: list[str]) -> None:
        self.__keywords = keywords
        self.__location = location

        keywords = self.__words_to_text(keywords)
        location = self.__words_to_text(location)
        self.__url = (f"https://www.linkedin.com/jobs/search?keywords={keywords}&location="
                      f"{location}&trk=guest_homepage-basic_guest_nav_menu_jobs")

    @property
    def keywords(self):
        return self.__keywords

    @property
    def location(self):
        return self.__location

    @property
    def url(self):
        return self.__url

    @staticmethod
    def __words_to_text(words: list[str]) -> str:
        return '%20'.join(words).replace(' ', '%20')

    def get_data(self, count: int = 20) -> list[dict[str, Any]]:
        link = self.__url
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        list_ = []
        job_cards = results.find_all("div", class_="base-card")

        job_cards = job_cards[:count]

        for job_card in job_cards:
            job_title = job_card.find("h3", class_="base-search-card__title")
            company_contry = job_card.find("h4", class_="base-search-card__subtitle")
            date = job_card.find("time", class_="job-search-card__listdate--new")
            job_link = job_card.find("a", class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")
            if date is not None:
                date = date['datetime'].split('-')
                date = datetime.date(*[int(elem) for elem in date])
            else:
                date = None

            list_.append({
                "job_title": job_title.get_text(strip=True) if job_title else None,
                "name_company": company_contry.get_text(strip=True) if company_contry else None,
                "date": date,
                "link": job_link['href'] if job_link else None
            })
        return list_
