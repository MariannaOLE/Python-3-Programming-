from html2text import html2text # learn more: https://python.org/pypi/html2text
import csv
import urllib.request
from bs4 import BeautifulSoup


with open('names.csv', 'w') as csvfile:
  fieldnames = ['item']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  writer.writeheader()


  url = 'http://www.asiaone.com/lottery'
  response = urllib.request.urlopen(url)
  data = response.read()
  soup = BeautifulSoup(data, "html.parser")
  for x in soup.findAll('div', {'class': "table-cell text-center ui header tiny"}):
    writer.writerow({'item': html2text(str(x)).strip()})
    
  
  
  