from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
driver = webdriver.Chrome()
names = []
prices = []
ratings = []
seller_percentage = []
with open('Extracted Links.csv', 'r') as file:
    data_set = [line.strip() for line in file]
for link in data_set:
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    item_list = soup.find('div', class_='"organic-list organic-list_G app-organic-search__list organic-list-gallery-wrapper')
    for item in item_list:
        name = item.find('div', class_='search-card-e-title')
        s_name = name.find('span')
        price = item.find('div', class_='search-card-e-price-main')
        s_price = price.find('data-aplus-clk')
        rating = item.find('span', class_='search-card-e-review')
        # Extract the percentage from the string
        # Append the data to respective lists
        names.append(name.text if name else 'None')
        prices.append(price.text if price else 'None')
        ratings.append(rating.text if rating else 'None')
    df = pd.DataFrame(
        {'Product Name': names, 'Price': prices, 'Condition': ratings})
    # Save the data to the CSV file in append mode
    df.to_csv('Products.csv', mode='a', header=False, index=False, encoding='utf-8')
driver.close()

base_url ="https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.historyItem_pos_0&tab=all&searchText=mobile+phones"
page_number = 1

while True:  # Use an infinite loop to continue scraping all pages
    url = f"{base_url}&page={page_number}"
    print(url)

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data for page {page_number}. Exiting.")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    main_class = soup.findAll("div", class_="organic-list organic-list_G app-organic-search__list organic-list-gallery-wrapper")

    for i in main_class:
        price = i.find("div", class_="search-card-e-price-main")
        name = i.find("h2", class_="search-card-e-title")
        print(name.text)
        print(price.text)
        # Find all strong tags within the main class
    #     strong_tags = sub_class.find_all('strong')
    #
    #     for strong_tag in strong_tags:
    #         strong_text = strong_tag.text
    #         print(strong_text)
    #
    # # Check if there's a "next page" link
    next_page_link = soup.find("a", class_="next")
    if next_page_link:
        page_number += 1  # Move to the next page
    else:
        print("No more pages to scrape.")
        break
