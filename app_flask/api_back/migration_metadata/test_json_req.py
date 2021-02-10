"""
Для примера
"""
import json
import requests


DEFAULT_JSON_OUT_PATH = 'test_json_out.json'

if __name__ == '__main__':

    with open('test_json.json', 'r', encoding='utf-8') as fobj:
        json_array = json.load(fobj)
        res = requests.post('http://localhost:5000/get_metadata', json=json_array)
        if res.ok:
            result_json = res.json()
            print(result_json)

