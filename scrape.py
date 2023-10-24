import requests
from bs4 import BeautifulSoup
import pandas as pd

def main_run():
    # Set the base URL and initialize a variable to track the current page number
    base_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=smartphone&_sacat=0"
    page_number = 1

    t_list = []
    price_list=[]
    shipping_list=[]
    sold_list=[]
    location_list=[]
    while page_number < 51:
        # Construct the URL for the current page
        url = f"{base_url}&_pgn={page_number}"  #  Adjust _ipg for the number of items per page

        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to retrieve data. Exiting.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="s-item__wrapper clearfix")

        for item in items:
            price = item.find("span", class_="s-item__price")
            if price:
                price_text = price.text.strip()
                price_list.append(price_text)
            else:
                price_text = "N/A"
                price_list.append(price_text)

            shipping = item.find("span", class_="s-item__shipping s-item__logisticsCost")
            if shipping:
                shipping_text = shipping.text.strip()
                shipping_list.append(shipping_text)
            else:
                shipping_text = "N/A"
                shipping_list.append(shipping_text)
            title_div = item.find("span", {'role': 'heading'})
            if title_div:
                title = title_div.text.strip()
                t_list.append(title)
            else:
                title = "N/A"
                t_list.append(title)
            sold = item.find("span", class_="BOLD")
            if sold:
                sold_text = sold.text.strip()
                sold_list.append(sold_text)
            else:
                sold_text = "N/A"
                sold_list.append(sold_text)
            location = item.find("span", class_="s-item__location s-item__itemLocation")
            if location:
                location_text = location.text.strip()
                location_list.append(location_text)
            else:
                location_text = "N/A"
                location_list.append(location_text)

        print(len(t_list))
        print(len(price_list))
        print(len(shipping_list))
        print(len(sold_list))
        print(len(location_list))

        next_button = soup.find("a", class_="pagination__next")
        if next_button:
            page_number += 1
            print("Your pagenumber",page_number)
            data = {'Title': t_list, 'Price': price_list, 'Shipping': shipping_list, 'Sold': sold_list,'Location': location_list}
            df = pd.DataFrame(data)
            # Save the DataFrame to a CSV file
            csv_file_path = "phone.csv"
            df.to_csv(csv_file_path, index=False, encoding='utf-8')
        else:
            print("No more pages. Exiting.")
            break

def main():
    main_run()

if __name__ == "__main__":
    main()
