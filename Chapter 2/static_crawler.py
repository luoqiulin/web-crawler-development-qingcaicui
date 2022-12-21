from email import header
import json
from os import makedirs
from os.path import exists
import requests
import logging
import re
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

url = 'https://api.bilibili.com/x/v2/reply/main?csrf=ece425a364823bec6185643f973de566&mode=3&next=4&oid=605444842&plat=1&type=1'

def scrape_page(url):
    """
    scrape page by url and return its html
    :param url: page url
    :return: html of page
    """
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

res = scrape_page(url)
print(type(res.decode(utf-8))


