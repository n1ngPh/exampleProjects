import pandas as pd
import json
from typing import Dict, List
import requests
import bs4
from urllib.parse import urljoin

import requests
import bs4
import json
from urllib.parse import urljoin
from typing import List, Dict


def check_valid(domain, href):
    if not href.startswith(domain):
        return False
    else:
        return True


def crawler(url, max_pages=100):

    return sorted(visited)


def task1(starting_links: List[str], json_filename: str) -> Dict[str, List[str]]:
    page_dict = {}

    for link in starting_links:
        page_dict[link] = crawler(link)

    with open(json_filename, "w") as outfile:
        json.dump(page_dict, outfile)

    return page_dict


starting_links = []

json_filename = "task1_my_full.json"

output = task1(starting_links, json_filename)
