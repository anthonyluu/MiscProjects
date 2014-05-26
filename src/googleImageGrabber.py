import json
import time
import urllib
import urllib.request
import os.path
import sys

# function to prompt user and make sure the string is useable
def search_link(prompt):
	'''
	@prompt: string - Prompt to ask user a question
	returns string
	'''
	# if the search has spaces, it will replace it
	search_text = input(prompt)
	search = search_text.replace(" ", "%20")
	return search
	
# function to download files given name and url
def download_files(name,url):
	'''
	@name: string - Name for file
	@url: string - URL to the download location online
	returns void
	'''
	downloadFile = urllib.request.urlopen(url);
	with open(name + ".jpg", "wb") as code:
		code.write(downloadFile.read());

# function to query and return raw json
def request_search(search, start):
	'''
	@search: string - Value to search
	@start: int - Not used much right now
	returns json_raw
	'''
	google_link_prefix = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="
	google_link_suffix = "&start="
	# creates the search query string
	search_query = google_link_prefix + search + google_link_suffix + str(start)
	req = urllib.request.urlopen(search_query);
	json_raw = json.loads(req.read().decode(req.headers.get_content_charset()))
	return json_raw

	
# Constants
prompt = "What would you like to download? "
img_download_links = []
img_names = []
start = 0
i = 0


# Main start
search = search_link(prompt)
json = request_search(search,start)
json_results = json['responseData']['results']
json_results_size = len(json_results)

while i < json_results_size:
	# gets the url from the returned json data
	img_link = json['responseData']['results'][i]['url']
	# splits the url to grab the clean name
	img_name = os.path.splitext(img_link.split('/')[-1])[0]
	
	# adding links and names to array
	# arrays not used for now
	img_download_links.append(img_link)
	img_names.append(img_name)
	
	print (img_link)
	print (img_name)
	print ('')
	
	download_files(img_name,img_link)
	i += 1


