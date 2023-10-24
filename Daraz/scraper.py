
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import os

def ReadFile_link(link, path):
    name_list, price_list, rating_list = [], [], []
    df = pd.read_csv(path)

    name_list += df['Name'].values.tolist()
    price_list += df['Price'].values.tolist()
    rating_list += df['Rating'].values.tolist()
    
    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    content = str(driver.page_source.encode())

    soup = BeautifulSoup(content, 'lxml')

    # for i in soup.find_all('div', class_="title--wFj93"):
    #     print(i.get_text())

    x = 0
    for i in soup.find_all('div', class_='info--ifj7U'):   #getting the whole content box count
        x += 1

    name, price, rating = '', '', ''
    # name = soup.find_all('div', class_='title--wFj93')[0].text
    # name = re.sub(r'\s+', ' ', name).strip()
    
    # price = soup.find_all('div', class_='price--NVB62')[0].text
    # price = re.sub(r'\s+', ' ', price).strip()

    # rating = soup.find_all('div', class_='rateAndLoc--XWchq')[0].find('div', class_='rating--ZI3Ol rate--DCc4j').find('span', class_='rating__review--ygkUy').text
    # rating = re.sub(r'\s+', ' ', rating).strip()

    # print(name)
    # print(price)
    # print(rating)

    for j in range(x):
        name = '-'
        price = '-'
        rating = '-'

        try:
            name = soup.find_all('div', class_='title--wFj93')[j].text
            name = re.sub(r'\s+', ' ', name).strip()
            
            price = soup.find_all('div', class_='price--NVB62')[j].text
            price = re.sub(r'\s+', ' ', price).strip()

            rating = soup.find_all('div', class_='rateAndLoc--XWchq')[j].find('div', class_='rating--ZI3Ol rate--DCc4j').find('span', class_='rating__review--ygkUy').text
            rating = re.sub(r'\s+', ' ', rating).strip()
        except:
            pass

        name_list.append(name)
        price_list.append(price)
        rating_list.append(rating)

    df = pd.DataFrame({'Name':name_list, 'Price':price_list, 'Rating':rating_list})
    df.to_csv(path, index=False, encoding='utf-8')

def main():
    os.system("cls")
    path = "daraz_data.csv"
    daraz_smartphones_urls = [
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=2",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=3",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=4",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=5",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=6",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=7",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=8",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=9",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=10",
        "https://www.daraz.pk/catalog/?spm=a2a0e.searchlist.0.0.691a2f68zMhF4G&_keyori=ss&from=input&q=smartphones&page=11",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=12",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=13",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=14",
        "https://www.daraz.pk/catalog/?spm=a2a0e.searchlist.0.0.72c62f68UyriDl&_keyori=ss&from=input&q=smartphones&page=15",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=16",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=17",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=18",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=19",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=20",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=21",
        "https://www.daraz.pk/catalog/?_keyori=ss&from=input&q=smartphones&spm=a2a0e.home.search.go.35e34076tc8Q7d&page=22"
    ]
    for i in range(14, len(daraz_smartphones_urls)):
        ReadFile_link(daraz_smartphones_urls[i], path)
        # ReadFile_link(i, path)
        print("--------------------------------------------------------------------------------------------------------------------")
        print("Done >>>>>>  ", i)
        print("--------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()