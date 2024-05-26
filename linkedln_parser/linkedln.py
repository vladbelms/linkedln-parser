import httpx
from bs4 import BeautifulSoup


class Linkedln:
    def __init__(self,URL):
        self.URL = URL
    def get_name(self):
        page = httpx.get(self.URL)
        results = BeautifulSoup(page.content, "html.parser")
        job_elements = results.find_all("h3", class_="base-search-card__title")
        for job_element in job_elements:
            print(job_element.text.strip())

