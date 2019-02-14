import json
import os
from collections import OrderedDict

responses = {x.split('.')[0]:json.load(open(f'locale/{x}', encoding='utf-8'), object_pairs_hook=OrderedDict) for x in os.listdir('locale')}

langs = list(responses.keys())

key = input("Introduce el nombre de la nueva clave: ")

for x in langs:
    value = input(f"Valor para \"{key}\" en el idioma \"{x}\": ")
    responses[x][key] = value.replace('\\n', os.linesep)
    with open(f'locale/{x}.json', 'w', encoding='utf-8') as f:
        json.dump(responses[x], f, indent=4)

with open('response_keys.json', 'w', encoding='utf-8') as f:
    json.dump(list(responses[langs[0]].keys()), f, indent=4)