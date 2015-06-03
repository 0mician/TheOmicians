from BeautifulSoup import BeautifulSoup
import requests

url = "http://crispr.u-psud.fr/crispr/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
links = soup.findAll('a', href=True)
bacteria_links = open('reports/bacteria_links_crispr.txt', 'w')
temp = []

for link in links:
    temp.append(link.get('href').encode('ascii'))

for link in temp:
    if ('/cgi-bin/crispr/SpecieProperties.cgi' in link):
        bacteria_links.write('http://crispr.u-psud.fr' + link + "\n")

bacteria_links.close()
