from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd  # Added pandas library import
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def FetchAndSave(link, num_pages):

    options = webdriver.ChromeOptions()
    service = Service(executable_path="C:\Chrome\chromedriver.exe")
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    content = str(driver.page_source.encode())
    soup = BeautifulSoup(content, 'lxml')
    all_links = []

    l = soup.find('div', class_="makers")
    links = l.find_all('a')
    for i in links:
        all_links.append(i.get('href'))

    driver.quit()  # Close the Chrome driver
    return all_links


def ReadFile_link(link, path):
    name_list = []
    display_list = []
    Ram_list = []
    df = pd.read_csv(path)
    name_list += df['Title'].values.tolist()
    display_list += df['Display'].values.tolist()
    Ram_list += df['Ram'].values.tolist()

    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    content = str(driver.page_source.encode())

    soup = BeautifulSoup(content, 'lxml')

    x = 0
    for i in soup.find_all('div',class_='article-info'):
        x += 1

    name, price, rating = '', '', ''
    for j in range(x - 1):
        name = '-'
        diplay = '-'
        Ram = '-'

        try:
            name = soup.find_all('div', class_='article-info')[j].find('h1', class_='specs-phone-name-title').text
            name = re.sub(r'\s+', ' ', name).strip()

            price = soup.find_all('div', class_='article-info')[j].find('strong', class_='accent').text
            price = re.sub(r'\s+', ' ', diplay).strip()

            rating = soup.find_all('div', class_='article-info')[j].find('strong', class_='accent accent-expansion').text
            rating = re.sub(r'\s+', ' ', Ram).strip()
        except:
            pass

        name_list.append(name)
        display_list.append(price)
        Ram_list.append(rating)

    df = pd.DataFrame({'Name': name_list, 'Price': display_list, 'Rating': Ram_list})
    df.to_csv("dat.csv", index=False, encoding='utf-8')


def main():
    link = ["https://www.gsmarena.com/samsung-phones-9.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p2.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p3.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p4.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p5.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p6.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p7.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p8.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p9.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p10.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p11.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p12.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p13.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p14.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p15.php",
            "https://www.gsmarena.com/samsung-phones-f-9-0-p16.php"]
    num_pages = 16  # Number of pages to scrape
    all_links = []  # Create a list to store all the links
    for i in link:
        links = FetchAndSave(i, num_pages)
        all_links.extend(links)  # Extend the list with the links from this iteration

    data = {'Link': all_links}  # Create a dictionary with the data

    df = pd.DataFrame(data)  # Create a DataFrame
    csv_file_path = "links.csv"
    df.to_csv(csv_file_path, index=False, encoding='utf-8')  # Save DataFrame to CSV
    for i in range(len(link)):
        ReadFile_link(link[i], csv_file_path)
        print("--------------------------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()
