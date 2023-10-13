
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
from simple_html_file_extracter import ReadFile_path
import os


def FetchAndSave(url, path):
    list_name = []
    list_price = []
    list_rating = []

    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # we want to establish the driver
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url)
    main_content = str(driver.page_source.encode())
    soup = BeautifulSoup(main_content,'lxml')
    # with open(path, 'w') as file:
    #     file.write(soup.prettify())

    for i in soup.find_all(class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section s-card-border"):
        # this is the whole card of data
        print(i)

    # for i in soup.find_all(class_="a-size-medium a-color-base a-text-normal"):
    #     list_name.append(i.text)
    # for i in soup.find_all(class_="a-size-medium a-color-base a-text-normal"):
    #     list_price.append(i.text)
    # for i in soup.find_all(class_="a-size-base s-underline-text"):
    #     list_rating.append(i.text)

    print(len(list_name))
    print(len(list_price))
    print(len(list_rating))

    # df = pd.DataFrame({'Product Name':list_name,'Price':list_price,'Rating':list_rating})
    # df.to_csv('amazon_data_final.csv', index=False, encoding='utf-8')

    # aSection = soup.find_all('a',attrs={'class','a-section'})
    # for x in aSection:
    #     aElement = x.select_one('a[href*=keyword]')
    #     title = aElement.find('span')
    #     print(title)
    # driver.quit()
    # soup = BeautifulSoup(main_content, 'html.parser')

def FetchAndSave_request(url, path):
    http_proxy = "http://23.224.102.222"
    https_proxy = "https://155.94.134.166"
    ftp_proxy = "ftp://23.224.102.222"

    proxies = {
        # "http" : http_proxy,
        "https" : https_proxy,
        # "ftp" : ftp_proxy
    }
    r = requests.get(url)
    with open(path, 'w') as file:
        file.write(r.text)

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

    x = 0
    for i in soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border'):
        x += 1

    name, price, rating = '', '', ''
    for j in range(x-1):
        name = '-'
        price = '-'
        rating = '-'

        try:
            name = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-size-medium a-color-base a-text-normal').text
            name = re.sub(r'\s+', ' ', name).strip()
            
            price = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-offscreen').text
            price = re.sub(r'\s+', ' ', price).strip()

            rating = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-size-base s-underline-text').text
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
    flipkart_url = "https://www.flipkart.com/search?q=smartphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    amazon_url = "https://www.amazon.com/s?k=smartphones&ref=nb_sb_noss"
    daraz_url = "https://www.daraz.pk/catalog/?q=smartphones&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34076tc8Q7d"
    imdb_url = "https://www.imdb.com/find/?q=horror%20movies&ref_=nv_sr_sm"
    phonedb_url = "https://phonedb.net/index.php?m=device&s=list"
    url = "http://127.0.0.1:5500/Learn/index.html#"
    amazon_new = "https://www.amazon.com/s?k=smartphones&page=5&qid=1696917556&ref=sr_pg_5"
    check = "https://www.amazon.com/s?k=smartphones&page=3&qid=1697021212&ref=sr_pg_3"
    path = "hello.html"
    store = "amazon_whole_data.csv"

    amazon_smartphones_urls = [
        "https://www.amazon.com/s?k=smartphones&qid=1697021706&ref=sr_pg_1",
        "https://www.amazon.com/s?k=smartphones&page=2&qid=1697025317&ref=sr_pg_2"
        "https://www.amazon.com/s?k=smartphones&page=3&qid=1697021212&ref=sr_pg_3",
        "https://www.amazon.com/s?k=smartphones&page=4&qid=1697021212&ref=sr_pg_4",
        "https://www.amazon.com/s?k=smartphones&page=5&qid=1696917556&ref=sr_pg_5",
        "https://www.amazon.com/s?k=smartphones&page=6&qid=1697021212&ref=sr_pg_6",
        "https://www.amazon.com/s?k=smartphones&page=7&qid=1697021212&ref=sr_pg_7",
        "https://www.amazon.com/s?k=smartphones&page=8&qid=1697021212&ref=sr_pg_8",
        "https://www.amazon.com/s?k=smartphones&page=9&qid=1697021212&ref=sr_pg_9",
        "https://www.amazon.com/s?k=smartphones&page=10&qid=1697025496&ref=sr_pg_10",
        "https://www.amazon.com/s?k=smartphones&page=11&qid=1697025485&ref=sr_pg_11",
        "https://www.amazon.com/s?k=smartphones&page=12&qid=1697025657&ref=sr_pg_12",
        "https://www.amazon.com/s?k=smartphones&page=13&qid=1697025664&ref=sr_pg_13",
        "https://www.amazon.com/s?k=smartphones&page=14&qid=1697025696&ref=sr_pg_14",
        "https://www.amazon.com/s?k=smartphones&page=15&qid=1697025737&ref=sr_pg_15"
    ]

    samsung = "https://www.samsung.com/pk/smartphones/all-smartphones/"

    flipkart_path = "flipkart_content.html"
    imdb_path = "imdb.html"
    amazon_path = "amazon_content.html"
    path = "amazon1.html"
    for i in range(len(amazon_smartphones_urls)):
        ReadFile_link(amazon_smartphones_urls[i], store)
        print("--------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()