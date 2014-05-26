import json
import time
import requests
import urllib
import urllib.request

def search_link(prompt):
	search = input(prompt)
	return search
	
def download_files(file_name):
	
	
	
googleLink = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="
suffix = "&start=%d"

prompt = "What would you like to download? "

search = search_link(prompt)
new_link = googleLink + search + suffix
start = 0


r = urllib.request.urlopen(new_link % start);
json = json.loads(r.read().decode(r.headers.get_content_charset()))

json_results = json['responseData']['results']
json_results_size = len(json_results)
url_download_links = []
i = 0
x = 0

while i < json_results_size:
	url_download_links.append(json['responseData']['results'][i]['url'])
	i += 1


while x < json_results_size:
	print (url_download_links[x])
	x += 1

