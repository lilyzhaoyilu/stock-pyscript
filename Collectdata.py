import urllib
import csv
from bs4 import BeautifulSoup as bs

DAYS = [1,2,3]

base_url = "http://www.nasdaq.com/symbol/%s/historical?tf=10y"

titles = ['Symbol', 'Date', 'Open', 'Closs']

source_csv = open('test.csv', 'r')
symbols = [i.strip() for i in source_csv.readlines()]


csvfile = open('testresults.csv', 'wb')
writer = csv.DictWriter(csvfile, fieldnames=titles)
writer.writerow(dict(zip(titles, titles)))


def spyder(symbol):
    url = base_url % symbol + "tf=10y"
    html = bs(urllib.urlopen(url).read())
    div = html.find("div", {'id': 'historicalContainer'})
    table = div.find("table")
    trs = table.findAll("tr")
    trs = [trs[-i] for i in DAYS]
    for i in trs:
        tds = i.findAll("td")
        data = {}
        data['Symbol'] = symbol
        data['Date'] = tds[0].getText().strip()
        data['Open'] = tds[1].getText().strip()
        data['Closs'] = tds[4].getText().strip()
        writer.writerow(data)


if __name__ == '__main__':
    for i in symbols[0: -1]:
        try:
            spyder(i)
        except:
            pass
