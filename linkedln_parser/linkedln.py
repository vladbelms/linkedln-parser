import httpx
from bs4 import BeautifulSoup


class Linkedln:
    def __init__(self, keywords: str, location: str):
        self.keywords = keywords.replace(" ", "%20")
        self.location = location.replace(" ", "%20")

    def get_name(self) -> None:
        link = f"https://www.linkedin.com/jobs/search?keywords={self.keywords}&location={self.location}trk=guest_homepage-basic_guest_nav_menu_jobs"
        page = httpx.get(link)
        results = BeautifulSoup(page.content, "html.parser")
        name_companies = results.find_all("h3", class_="base-search-card__title")
        country_companies = results.find_all("h4", class_="base-search-card__subtitle")
        for name_company in name_companies:
            for country_company in country_companies:
                job_stats = [name_company.text.strip(), country_company.text.strip()]
                print(job_stats)
