from typing import Any
import datetime
import httpx
from bs4 import BeautifulSoup


class LinkedIn:
    def __init__(self, keywords: list[str], location: list[str]) -> None:
        self.__keywords = keywords
        self.__location = location

        keywords = self.__words_to_text(keywords)
        # location = self.__words_to_text(location)
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

    def get_linkedin_data(self, count: int = 20) -> list[dict[str, Any]]:
        link = self.__url
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        list_ = []
        job_cards = results.find_all("div", class_="base-search-card__info")

        job_cards = job_cards[:count]

        for job_card in job_cards:
            job_title = job_card.find("h3", class_="base-search-card__title")
            company_contry = job_card.find("h4", class_="base-search-card__subtitle")
            date = job_card.find("time", class_="job-search-card__listdate")
            date = date['datetime'].split('-')
            date = datetime.date(*[int(elem) for elem in date])

            list_.append({
                "job_title": job_title.get_text(strip=True),
                "name_company": company_contry.get_text(strip=True),
                "date": date
            })
        return list_
