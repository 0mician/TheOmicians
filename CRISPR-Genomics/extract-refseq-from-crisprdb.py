from BeautifulSoup import BeautifulSoup
import requests

bacteria_links = open("bacteria_links_crispr.txt", "r")
info = open("bacteria_info_crisprdb.txt", "w")

for links in bacteria_links:
    refseq.write("#####\n")
    r = requests.get(links.rstrip("\n"))
    data = r.text
    soup = BeautifulSoup(data)
    name = soup.h1.contents[0].encode("ascii").lstrip(" ").rstrip(" ")

    table = soup.find('table', attrs={'class':'primary_table','width':'100%'})
    table_body = table.find('tbody')
    rows = table_body.findAll("tr")

    tds = []
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        tds.append(cols)

    for i in range(0,len(tds)):
        info.write(name + "\t" +
                   "Topology: " + tds[i][0].encode("ascii") + "\t" +
                   "RefSeq: " + tds[i][1].encode("ascii") + "\t" +
                   "GenBankID: " + tds[i][2].encode("ascii") + "\t" +
                   "Info: " + tds[i][3].encode("ascii") + "\t\n")

info.close()
