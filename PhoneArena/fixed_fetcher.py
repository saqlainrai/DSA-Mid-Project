
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import os

def ReadFile_link(link, path):
    name_list, price_list, rating_list, display_list, camera_list, hardware_list, storage_list, hardware_list = [], [], [], [], [], [], [], []

    # df = pd.read_csv(path)
    # name_list += df['Name'].values.tolist()
    # price_list += df['Price'].values.tolist()
    # rating_list += df['Rating'].values.tolist()
    
    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    content = str(driver.page_source.encode())

    soup = BeautifulSoup(content, 'lxml')

    # x = 0
    # for i in soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border'):
    #     x += 1

    name, price, rating = '', '', ''
    display = "-"
    camera = "-"
    hardware = "-"
    storage = "-"
    battery = "-"
    # for j in range(x-1):
    name = '-'
    price = '-'
    rating = '-'

    # name = soup.find('section', class_= "page__section page__section_quickSpecs").find('header').text
    # print(name)
    display = soup.find('a', class_= "widgetQuickSpecs__link display").find('p', class_= "widgetQuickSpecs__title_paragraph").text
    print(display)
    camera = soup.find('section', class_= "widgetQuickSpecs__title_paragraph").text
    print(camera)
    hardware = soup.find('section', class_= "widgetQuickSpecs__title_paragraph").text
    print(hardware)
    battery = soup.find('section', class_= "widgetQuickSpecs__title_paragraph").text
    print(battery)  

    # try:
    #     name = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-size-medium a-color-base a-text-normal').text
    #     name = re.sub(r'\s+', ' ', name).strip()
        
    #     price = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-offscreen').text
    #     price = re.sub(r'\s+', ' ', price).strip()

    #     rating = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section puis-card-border')[j].find('span', class_='a-size-base s-underline-text').text
    #     rating = re.sub(r'\s+', ' ', rating).strip()
    # except:
    #     pass

    # name_list.append(name)
    # price_list.append(price)
    # rating_list.append(rating)

    df = pd.DataFrame({'Name':name_list, 'Price':price_list, 'Rating':rating_list})
    df.to_csv(path, index=False, encoding='utf-8')

def main():
    os.system("cls")
    website_link = "https://www.phonearena.com/phones/Honor-Magic-V2_id12194"
    path = "phonearena_data.csv"

    ReadFile_link(website_link, path)

if __name__ == "__main__":
    main()