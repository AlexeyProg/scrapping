from encodings import utf_8
import requests
from bs4 import BeautifulSoup


# url = "https://www.avito.ru/moskva_i_mo/transport"

names = []

# response = requests.get(url).text

# with open('avitotest.html','w', encoding="utf8") as file:
#     file.write(response)

#good html

with open('avitotest.html','r',encoding="utf8") as file:
    content = file.read()

    soup = BeautifulSoup(content,'lxml')

# cars_names = soup.find_all('h3', class_= 'title-root-zZCwT')

# for item in cars_names:
#     names.append(item.text)
# print(names)
prices = []
newnames = []
cars_price = soup.find_all('div', class_= 'styles-item-W5Z4K')
for i in cars_price:
    pr = i.find('span',class_= 'price-price-JP7qe')
    prices.append(pr.text)
    newname = i.find('h3',class_ = 'title-root-zZCwT')
    newnames.append(newname.text)

#print(prices)
# print(newnames)
dictionary = dict(zip(newnames,prices))
print(dictionary)

file.close()