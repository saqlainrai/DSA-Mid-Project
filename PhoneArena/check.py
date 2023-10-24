
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

def ReadFile_link(link, path):
    name_list, price_list, display_list, camera_list, hardware_list, storage_list, battery_list = [], [], [], [], [], [], []

    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    content = str(driver.page_source.encode())
    soup = BeautifulSoup(content, 'lxml')

    # whole section of Details has this class
    # page__section page__section_quickSpecs

    name, price, display, camera, hardware, storage, battery = '-', '-', '-', '-', '-', '-', '-'
    try:
        name = soup.find('section', class_= "page__section page__section_quickSpecs").find('header').text
        print(name)
        display = soup.find('a', class_= "widgetQuickSpecs__link display").find('p', class_= "widgetQuickSpecs__title_paragraph").text
        print(display)
        camera = soup.find('div', class_= "widgetQuickSpecs__main").find('a', class_= "widgetQuickSpecs__link camera").find('p' ,class_="widgetQuickSpecs__title_paragraph").text
        print(camera)
        hardware = soup.find('div', class_= "widgetQuickSpecs__main").find('a', class_= "widgetQuickSpecs__link hardware").find('p' ,class_="widgetQuickSpecs__title_paragraph").text
        print(hardware)
        storage = soup.find('div', class_= "widgetQuickSpecs__main").find('a', class_= "widgetQuickSpecs__link storage").find('p' ,class_="widgetQuickSpecs__title_paragraph").text
        print(storage)
        battery = soup.find('div', class_= "widgetQuickSpecs__main").find('a', class_= "widgetQuickSpecs__link battery").find('p' ,class_="widgetQuickSpecs__title_paragraph").text
        print(battery)
        price = soup.find('section', class_= "phone__section phone__section_widget_shopLinks").find('div', class_= "widgetShopLinks").find('span', class_="price").text
        print(price)
    except:
        print("Exception was Thrown")

    df = pd.DataFrame({'Name':name, 'Price':price, 'Display':display, 'Camera':camera, 'Hardware':hardware, 'Storage':storage, 'Battery':battery}, index=[0])
    df.to_csv(path, mode='a', index=False, header=False, encoding='utf-8')

def main():
    os.system("cls")
    path = "phonearena_data.csv"
    main_df = pd.read_csv('phonearena_link.csv')
    name = main_df['Links'].values.tolist()
    # print(len(name))              8752

    for i in range(1800, len(name)):
        link = name[i]
        ReadFile_link(link, path)
        print(str(i) + "  Done  >>>>>>>> " + link)

    link = "https://www.phonearena.com/phones/Blackview-Tab-80_id12206"
    # ReadFile_link(link, path)

if __name__ == '__main__':
    main()