import time
import sys
import requests
import yaml
from requests.utils import quote
from bs4 import BeautifulSoup

dict_root = "https://jisho.org/search/"

def fetch_kanji_props(term):
    query_uri = dict_root + quote(term) + "%20%23kanji"
    response = requests.get(query_uri)
    soup = BeautifulSoup(response.content, 'html.parser')
    stroke_count = soup.find(class_="kanji-details__stroke_count").find('strong').text
    kun_yomi = soup.find(class_="dictionary_entry kun_yomi")
    if kun_yomi:
        children = kun_yomi.findAll('a')
        kun_yomi = list(map(lambda x: x.text.strip(), children))
    else:
        kun_yomi = "No kun-yomi"
    # on_yomi class is used non-semantically, need to select one with readings
    on_yomi = soup.findAll(class_="dictionary_entry on_yomi")
    true_on_yomi = None
    for el in on_yomi:
        if el.find(class_="kanji-details__main-readings-list"):
            true_on_yomi = el
    on_yomi = true_on_yomi.findAll('a')
    on_yomi = list(map(lambda x: x.text.strip(), on_yomi))
    meanings = soup.find(class_="kanji-details__main-meanings").text.strip().split(", ")
    return [meanings, stroke_count, kun_yomi, on_yomi]

if len(sys.argv) > 1:
    lexicon_src = sys.argv[1]
    input_f = open(lexicon_src, "r", encoding="utf-8")
    kanji_data = dict()
    kanji_in_order = []
    for line in input_f:
        query_term = line.rstrip()
        props = fetch_kanji_props(query_term)
        kanji_data[query_term] = {"stroke_count": props[1], "meanings": props[0], "kun_yomi": props[2], "on_yomi": props[3]}
        kanji_in_order.append(query_term)
        time.sleep(1)

    final_dict = {
        "kanji_properties": kanji_data,
        "kanji_in_order": kanji_in_order
    }
    with open("output.yaml", 'w', encoding="utf-8") as fp:
        yaml.dump(final_dict, stream=fp, allow_unicode=True, sort_keys=False)
    fp.close()