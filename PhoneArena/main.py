
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

def ReadFile_link(link, path):
    service = Service(executable_path="C:\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    content = str(driver.page_source.encode())

    soup = BeautifulSoup(content, 'lxml')

    link_list = []

    j = 0
    for i in soup.find_all('div', class_="widget widget-tilePhoneCard"):
        text = i.find('a', class_="thumbnail")
        if text:
            text = text.get('href')
            print(text)
            link_list.append(text)
            print(j, " >>> ------------------------------------------------------------------------------------------------------------------------")
            j += 1
        else:
            print("Operation Not performed Successfully")

    print("-------------------------------------------------------------------------------------------------------------------")
    print(len(link_list), " >>>>>>>>>>>>>>", link)
    print("-------------------------------------------------------------------------------------------------------------------")

    df = pd.DataFrame({'Link': link_list})
    df.to_csv(path, mode='a', index=False, header=False, encoding='utf-8')

def main():
    os.system("cls")
    website_link = "https://www.phonearena.com/phones/Honor-Magic-V2_id12194"
    path = "phonearena_link.csv"
    whole_phones = "https://www.phonearena.com/phones"

    array =[
        # "https://www.phonearena.com/phones/page/11",
        # "https://www.phonearena.com/phones/page/12",
        # "https://www.phonearena.com/phones/page/13",
        # "https://www.phonearena.com/phones/page/14",
        # "https://www.phonearena.com/phones/page/15",
        # "https://www.phonearena.com/phones/page/16",
        # "https://www.phonearena.com/phones/page/17",
        # "https://www.phonearena.com/phones/page/18",
        # "https://www.phonearena.com/phones/page/19",
        # "https://www.phonearena.com/phones/page/20",
        # "https://www.phonearena.com/phones/page/21",
        # "https://www.phonearena.com/phones/page/22",
        # "https://www.phonearena.com/phones/page/23",
        # "https://www.phonearena.com/phones/page/24",
        # "https://www.phonearena.com/phones/page/25",
        # "https://www.phonearena.com/phones/page/26",
        # "https://www.phonearena.com/phones/page/27",
        # "https://www.phonearena.com/phones/page/28",
        # "https://www.phonearena.com/phones/page/29",
        # "https://www.phonearena.com/phones/page/30",
        # "https://www.phonearena.com/phones/page/31",
        # "https://www.phonearena.com/phones/page/32",
        # "https://www.phonearena.com/phones/page/33",
        # "https://www.phonearena.com/phones/page/34",
        # "https://www.phonearena.com/phones/page/35",
        # "https://www.phonearena.com/phones/page/36",
        # "https://www.phonearena.com/phones/page/37",
        # "https://www.phonearena.com/phones/page/38",
        # "https://www.phonearena.com/phones/page/39",
        # "https://www.phonearena.com/phones/page/40",
        # "https://www.phonearena.com/phones/page/41",
        # "https://www.phonearena.com/phones/page/42",
        # "https://www.phonearena.com/phones/page/43",
        # "https://www.phonearena.com/phones/page/44",
        # "https://www.phonearena.com/phones/page/45",
        # "https://www.phonearena.com/phones/page/46",
        # "https://www.phonearena.com/phones/page/47",
        # "https://www.phonearena.com/phones/page/48",
        # "https://www.phonearena.com/phones/page/49",
        # "https://www.phonearena.com/phones/page/50",
        # "https://www.phonearena.com/phones/page/51",
        # "https://www.phonearena.com/phones/page/52",
        # "https://www.phonearena.com/phones/page/53",
        # "https://www.phonearena.com/phones/page/54",
        # "https://www.phonearena.com/phones/page/55",
        # "https://www.phonearena.com/phones/page/56",
        # "https://www.phonearena.com/phones/page/57",
        # "https://www.phonearena.com/phones/page/58",
        # "https://www.phonearena.com/phones/page/59",
        # "https://www.phonearena.com/phones/page/60",
        # "https://www.phonearena.com/phones/page/61"
        # "https://www.phonearena.com/phones/page/62",
        # "https://www.phonearena.com/phones/page/63",
        # "https://www.phonearena.com/phones/page/64",
        # "https://www.phonearena.com/phones/page/65",
        # "https://www.phonearena.com/phones/page/66",
        # "https://www.phonearena.com/phones/page/67",
        # "https://www.phonearena.com/phones/page/68",
        # "https://www.phonearena.com/phones/page/69",
        # "https://www.phonearena.com/phones/page/70",
        # "https://www.phonearena.com/phones/page/71",
        # "https://www.phonearena.com/phones/page/72",
        # "https://www.phonearena.com/phones/page/73",
        # "https://www.phonearena.com/phones/page/74",
        # "https://www.phonearena.com/phones/page/75",
        # "https://www.phonearena.com/phones/page/76",
        # "https://www.phonearena.com/phones/page/77",
        # "https://www.phonearena.com/phones/page/78",
        # "https://www.phonearena.com/phones/page/79",
        # "https://www.phonearena.com/phones/page/80",
        # "https://www.phonearena.com/phones/page/81",
        # "https://www.phonearena.com/phones/page/82",
        # "https://www.phonearena.com/phones/page/83",
        # "https://www.phonearena.com/phones/page/84",
        # "https://www.phonearena.com/phones/page/85",
        # "https://www.phonearena.com/phones/page/86",
        # "https://www.phonearena.com/phones/page/87",
        "https://www.phonearena.com/phones/page/88",
        "https://www.phonearena.com/phones/page/89",
        "https://www.phonearena.com/phones/page/90",
        "https://www.phonearena.com/phones/page/91",
        "https://www.phonearena.com/phones/page/92",
        "https://www.phonearena.com/phones/page/93",
        "https://www.phonearena.com/phones/page/94",
        "https://www.phonearena.com/phones/page/95",
        "https://www.phonearena.com/phones/page/96",
        "https://www.phonearena.com/phones/page/97",
        "https://www.phonearena.com/phones/page/98",
        "https://www.phonearena.com/phones/page/99",
        "https://www.phonearena.com/phones/page/100",
        "https://www.phonearena.com/phones/page/101",
        "https://www.phonearena.com/phones/page/102",
        "https://www.phonearena.com/phones/page/103",
        "https://www.phonearena.com/phones/page/104",
        "https://www.phonearena.com/phones/page/105",
        "https://www.phonearena.com/phones/page/106",
        "https://www.phonearena.com/phones/page/107",
        "https://www.phonearena.com/phones/page/108",
        "https://www.phonearena.com/phones/page/109",
        "https://www.phonearena.com/phones/page/110",
        "https://www.phonearena.com/phones/page/111",
        "https://www.phonearena.com/phones/page/112",
        "https://www.phonearena.com/phones/page/113",
        "https://www.phonearena.com/phones/page/114",
        "https://www.phonearena.com/phones/page/115",
        "https://www.phonearena.com/phones/page/116",
        "https://www.phonearena.com/phones/page/117",
        "https://www.phonearena.com/phones/page/118",
        "https://www.phonearena.com/phones/page/119",
        "https://www.phonearena.com/phones/page/120"
    ]

    for x in range(121, 254):
        gene = "https://www.phonearena.com/phones/page/" + str(x)
        ReadFile_link(gene, path)

if __name__ == "__main__":
    main()