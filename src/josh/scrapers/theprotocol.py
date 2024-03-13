"""Scraper for theprotocol.it website."""

from typing import Any
import bs4
import requests
from lxml import etree

base_url = "https://theprotocol.it"
url = "https://theprotocol.it/filtry/python;t/backend,big-data-science,ai-ml,qa-testing;sp/trainee,assistant,junior;p/krakow;wp"

resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.content, "html.parser")


# tree = etree.parse(resp.content, etree.HTMLParser())
dom = etree.HTML(str(soup))


xp_elems = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/section[2]/section[1]/div/div/div[1]/div/a"  # noqa
raw_elems = dom.xpath(xp_elems)

assert isinstance(raw_elems, list)

results: list[dict[str, Any]] = []
for raw_elem in raw_elems:
    assert isinstance(raw_elem, etree._Element)
    soup_i = bs4.BeautifulSoup(etree.tostring(raw_elem), "html.parser")
    a_i = soup_i.contents[0]
    assert isinstance(a_i, bs4.Tag)

    # Get URL (href)
    partial_url_i = a_i['href']
    full_url_i = f"{base_url}{partial_url_i}"

    # Get label for the offer

    result_i = {
        "label": a_i.get("aria-label", "NO LABEL"),
        "full_url": full_url_i,
    }
    results.append(result_i)

