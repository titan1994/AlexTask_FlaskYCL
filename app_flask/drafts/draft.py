"""
Черновик
"""
from json import dump as jsd, load as jsl, dumps as str_jsd
from pathlib import Path

DEFAULT_JSON_METADATA_PATH = Path().cwd() / Path('../documents/front_back_interaction/json_sdmx_ex2.json')

with open(DEFAULT_JSON_METADATA_PATH, 'r') as fobj:
    data_settings_json = jsl(fobj)

print(data_settings_json)

with open(DEFAULT_JSON_METADATA_PATH, 'w') as fobj:
    jsd(data_settings_json, fobj, indent=4)