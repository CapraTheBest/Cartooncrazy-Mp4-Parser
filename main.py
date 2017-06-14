import re, cfscrape, requests, config, subprocess, sys
from bs4 import BeautifulSoup

def usage():
	print('[-] Usage: python main.py [url]')
	print("It's a WIP but it gets the job done. For now it only supports cartooncrazy.me")

def main():
	if len(sys.argv) == 2:
		url = sys.argv[1]
		if('cartooncrazy' in url):
			print('[+]Waiting for request to complete...')
			scraper = cfscrape.create_scraper()

			soup = BeautifulSoup(scraper.get(url).content, "html.parser")
			print('[+]I think I got something')
			link1 = soup.find('iframe')['src']
			if config.DEBUG:
				print(link1)
			print('[+]Going Deeper')

			response = requests.get(link1)
			soup1 = BeautifulSoup(response.content, "html.parser")
			link2 = soup1.find('iframe')['src']
			if config.DEBUG:
				print(link2)
			print('[+]Going EVEN Deeper')

			response1 = requests.get(link2)
			soup2 = BeautifulSoup(response1.content, "html.parser")
			candidates = re.findall('(file).+\"(.*?)\"', str(soup2.contents))
			for mp4_url in candidates:
				if('mp4' in mp4_url[1]):
					print('Success!')
					subprocess.call([config.VLC_FOLDER, mp4_url[1]])
					break
				else:
					print('We failed :(')
		else:
			print('[-]Invalid URL')
	else:
		usage()
	
	
if __name__ == '__main__':
    main()