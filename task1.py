import requests
import pprint 
import json

def get_superhero():
	url = "https://akabab.github.io/superhero-api/api/all.json"
	resp = requests.get(url)
	if resp.status_code == 200:
		resp = resp.text
		resp = json.loads(resp)
		return resp
	else:
		message = 'Error'
		return message

def best_superhero():
	dict_heros = {}
	for item in superheroes:
		name = item['name']
		if name in list_name:
			key = name
			list_powerstats = item['powerstats']
			value = list_powerstats['intelligence']
			dict_heros[key] = value
			max_intelligence = max(dict_heros.values())
			max_key = max(dict_heros, key=dict_heros.get)
	return f'Самый умный супергерой {max_key} с уровнем интеллекта {max_intelligence}'

	if len(dict_heros) == 0:
		return f'По заданным данным {list_name} и {powerstats} ничего не нашлось'
		

superheroes = get_superhero()
list_name = ['Hulk', 'Captain America', 'Thanos']
powerstats = 'intellience'

print(best_superhero())
