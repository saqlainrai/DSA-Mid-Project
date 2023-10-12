import requests
from selenium import webdriver

def FetchAndSaveDataToFile(url, path):
    response = requests.get(url)
    with open(path, 'w') as f:
        f.write(response.text)

def main():
    url = "Assalam o alakum
    path = "data/times.html"
    FetchAndSaveDataToFile(url, path)

if __name__ == '__main__':
    main()
