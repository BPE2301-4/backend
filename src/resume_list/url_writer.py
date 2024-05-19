from ..core import session, Url
from typing import List
import requests
from bs4 import BeautifulSoup


def append_one_url(url: str):
    query = Url(url=url)
    session.add(query)
    session.commit()


def append_many_url(list_of_url: List[str]):
    query = [Url(url=x) for x in list_of_url]
    session.add_all(query)
    session.commit()


def get_url_from_request(post: str):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'
            }
    response = requests.get(post, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        return response.status_code

