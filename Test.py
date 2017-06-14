import re, cfscrape, requests, config, subprocess
from bs4 import BeautifulSoup

url = 'http://ww1.cartooncrazy.me/watch/family-guy-season-14-episode-1-peternormal-activity/'

print('[+]Waiting for request to complete...')
scraper = cfscrape.create_scraper()

soup = BeautifulSoup(scraper.get(url).content, "html.parser")
print('[+]I think I got something')
link1 = soup.find('iframe')['src']
print(link1)
print('[+]Going Deeper')

response = requests.get(link1)
soup1 = BeautifulSoup(response.content, "html.parser")
link2 = soup1.find('iframe')['src']
print(link2)
print('[+]Going EVEN Deeper')

response1 = requests.get(link2)
soup2 = BeautifulSoup(response1.content, "html.parser")
Final_Url = re.findall('(file).+\"(.*?)\"', str(soup2.contents))
for x in Final_Url:
	if('mp4' in x[1]):
		print('Success!')
		#print(x[1].replace("&", "^&"))
		subprocess.call([config.VLC_FOLDER, x[1].replace("&", "^&")], shell=True)
		break
	else:
		print('We failed :(')
