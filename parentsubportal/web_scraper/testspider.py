from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("https://www.disability-grants.org/")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True, text=True):
    print(link['href'], link.text)
