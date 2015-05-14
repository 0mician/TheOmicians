from BeautifulSoup import BeautifulSoup
import requests

url = "http://crispr.u-psud.fr/crispr/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
links = soup.findAll('a', href=True)
bacteria_links = []
temp = []

for link in links:
    temp.append(link.get('href').encode('ascii'))

for link in temp:
    if ('/cgi-bin/crispr/SpecieProperties.cgi' in link):
        bacteria_links.append(link)

f = open('bacteria_links_crispr', 'w')

for link in bacteria_links[0:10]:
    f.write('http://crispr.u-psud.fr' + link + "\n")

f.close()
