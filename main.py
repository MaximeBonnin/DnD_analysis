# https://raw.githubusercontent.com/oganm/dnddata/master/data-raw/dnd_chars_unique.json


import requests
import json

# -----------------

# dnd_chars_all.json OR dnd_chars_unique.json

url = "https://raw.githubusercontent.com/oganm/dnddata/master/data-raw/dnd_chars_unique.json"

with requests.get(url) as data:
    print(data.text)