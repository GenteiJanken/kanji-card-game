import time
import sys
import requests
from requests.utils import quote
from bs4 import BeautifulSoup

dict_root = "https://jisho.org/search/"

def fetch_kanji_props(term):
    term_stripped = term.rstrip()
    query_uri = dict_root + quote(term_stripped) + "%20%23kanji"
    response = requests.get(query_uri)
    soup = BeautifulSoup(response.content, 'html.parser')
    stroke_count = soup.find(class_="kanji-details__stroke_count").find('strong').text
    kun_yomi = soup.find(class_="dictionary_entry kun_yomi").findAll('a')
    kun_yomi = list(map(lambda x: x.text, kun_yomi))
    # on_yomi class is used non-semantically, need to select one with readings
    on_yomi = soup.findAll(class_="dictionary_entry on_yomi")
    true_on_yomi = None
    for el in on_yomi:
        if el.find(class_="kanji-details__main-readings-list"):
            true_on_yomi = el
    on_yomi = true_on_yomi.findAll('a')
    on_yomi = list(map(lambda x: x.text, on_yomi))
    meanings = soup.find(class_="kanji-details__main-meanings").text.strip().split(", ")
    return [meanings, stroke_count, kun_yomi, on_yomi]

if len(sys.argv) > 1:
    lexicon_src = sys.argv[1]
    input_f = open(lexicon_src, "r", encoding="utf-8")
    for line in input_f:
        props = fetch_kanji_props(line)
        time.sleep(1)
