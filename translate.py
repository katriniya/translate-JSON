#! /usr/bin/env python
# coding: utf-8
import json, re, requests, sys


URL_TRANSLATE_YANDEX= "https://translate.yandex.net/api/v1.5/tr.json/translate"
TOKKEN = "KEY" # enter YOUR key https://translate.yandex.ru/developers/keys
LANG = "en-ru" 


ORIGIN_FILE = 'english.json'
TRANSLATE_FILE = 'russian.json'

with open(ORIGIN_FILE, 'r') as trans_file:
	templates = json.load(trans_file)
	
with open(ORIGIN_FILE, 'r') as trans_file:
	translate_file_read = trans_file.read()

for country_name in (templates["data"]):

	normalize_country_name = str(country_name["name"]).replace(' ','+') #replace space of +

	url = URL_TRANSLATE_YANDEX + "?key=" + TOKKEN + "&text=" + normalize_country_name + "&lang=" + LANG
	print (url)

	requests_translate_post = requests.post(url)

	requests_translate_post = requests_translate_post.json()

	
	translate_file_read=translate_file_read.replace(country_name["name"], str(requests_translate_post["text"][0]), 1)

	with open(TRANSLATE_FILE, 'w',encoding="utf-8") as file:
		file.write(translate_file_read)

with open(TRANSLATE_FILE, 'w', encoding="utf-8") as file:
	file.write(translate_file_read)
