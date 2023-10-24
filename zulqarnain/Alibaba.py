from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'C:\Chrome\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
page = 1



titleList = []
priceList = []
#min_order_List = []
#yearList = []
rating_List = []
#shippinglist = []
# votesList = []
# storyList = []
# meta_scoreList = []
# directorList = []
# starsList = []
voteList = []

url = 'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.dd4d1ac8Jy2Lqm&fsb=y&IndexArea=product_en&keywords=laptop&tab=all&&page=1'

while page < 101:
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        for a in soup.findAll('div', attrs={'class', 'card-info list-card-layout__info'}):
            name = a.find('h2', class_='search-card-e-title').find('span')
            price = a.find('div', class_='search-card-e-price-main')
            #order = a.find('div', class_='search-card-m-sale-features__item')
            #year = a.find('a',class_='search-card-e-supplier__year').find('span')
            rating = a.find('span',class_='search-card-e-review')
            # year = a.find('span', attrs={'class': 'lister-item-year text-muted unbold'})
            # genre = a.find('span', attrs={'class': 'genre'})
            # time = a.find('span', attrs={'class': 'runtime'})
            # pg = a.find('span', attrs={'class': 'certificate'})
            # rating = a.find('strong')
            # vote = a.find('span', attrs={'name': 'nv'})
            # storyLine = a.find_all('p', attrs={'class': 'text-muted'})
            # score = a.find('span', attrs={'class': 'metascore'})
            # metadata = a.find_all('p')
            # print(metadata)

            if name is not None:
                titleList.append(name.text)
            else:
                titleList.append('None')
            if price is not None:
                priceList.append(price.text)
            else:
                priceList.append('None')
            if rating is not None:
                rate = rating.text.split()
                #voteList.append(rate[1].strip('()'))
                rating_List.append(rate[0])
            else:
                #voteList.append(0)
                rating_List.append('None')
        base_url = "https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.keydown__Enter&tab=all&searchText=laptop"
        page = page + 1
        url = base_url + str(page)
        print(url)


    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break

df = pd.DataFrame({'Title Name': titleList, 'Price': priceList, 'Rating': rating_List})
df.to_csv('alibaba.csv', index=False, encoding='utf-8', mode='a')
