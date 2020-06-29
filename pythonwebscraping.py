
#Requirements
#pip3 install requests
#pip3 install bs4

from bs4 import BeautifulSoup

import requests


url="https://techcrunch.com/" #change this url to the site you want to scrap.

source=requests.get(url)


soup=BeautifulSoup(source.text,'html')


title=soup.find('title') 
print("this is with html tags :",title)

qwery=soup.find('h1') 


print("this is without html tags:",qwery.text) 


links=soup.find('a')
print(links)





print(links['href']) 


print(links['class'])





many_link=soup.find_all('a') 
total_links=len(many_link)
print("total links in my website :",total_links)
print()
for i in many_link[:6]: 
    print(i)

second_link=many_link[1] 
print(second_link)
print()
print("href is :",second_link['href']) 



nested_div=second_link.find('div')

print(nested_div)
print()

z=(nested_div['class'])
print(z)
print(type(z))
print()

print("class name of div is :"," ".join(nested_div['class'])) 




