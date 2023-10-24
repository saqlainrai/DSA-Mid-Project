import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=85f034bd-0806-42cd-8af2-ccdcd418cf4e&as-backfill=on&page=35"
page_number = 1

t_list = []
price_list = []
Rom_list = []
Ram_list = []
display_list = []
rating_list = []
battery_list = []

while page_number < 250:
    # Construct the URL for the current page
    url = f"{base_url}&page={page_number}"
    print(url)
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data. Exiting.")
        break
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")

    items=soup.find_all("div", attrs={"class=":"_2kHMtA"})
    print(items)
    for item in items:
        print("check")
        price = item.find("div", class_="_30jeq3 _1_WHN1")
        if price:
            price_text = price.text.strip()
            price_list.append(price_text)
        else:
            price_text = "N/A"
            price_list.append(price_text)

        title_div = item.find("div", class_="_4rR01T")
        if title_div:
            title = title_div.text.strip()
            t_list.append(title)
        else:
            title = "N/A"
            t_list.append(title)

        ul_element = item.find("ul", class_="_1xgFaf")
        if ul_element:
            li_elements = ul_element.find_all("li")
            if li_elements:
                Rom_text = li_elements[0].text.strip()
                split_text = [part.strip() for part in Rom_text.split('|')]

                # Handle cases where there may not be two parts separated by '|'
                try:
                    ram, rom = split_text
                except ValueError:
                    # In cases where there is only one value, assign it to either `ram` or `rom`
                    ram = split_text[0]
                    rom = "N/A"
                display_text = li_elements[1].text.strip()
                battery_text = li_elements[3].text.strip()
            else:
                Rom_text = "N/A"
                display_text = "N/A"
                battery_text = "N/A"
            Rom_list.append(rom)
            Ram_list.append(ram)
            display_list.append(display_text)
            battery_list.append(battery_text)
        else:
            Rom_list.append("N/A")
            Ram_list.append("N/A")
            display_list.append("N/A")
            battery_list.append("N/A")
        rating = item.find("div", class_="_3LWZlK")
        if rating:
            rating_text = rating.text.strip()
            rating_list.append(rating_text)
        else:
            rating_text = "N/A"
            rating_list.append(rating_text)

        print("Title:", title)
        print("Price:", price_text)
        print("Rom:", rom)
        print("Ram:", ram)
        print("Display:", display_text)
        print("Rating:", rating_text)
        print("battery:", battery_text)

    page_number += 1
    print("Your page number:", page_number)

# Create a DataFrame from the scraped data
    data = {
        'Title': t_list,
        'Price': price_list,
        'Rom': Rom_list,
        'Ram': Ram_list,
        'Display': display_list,
        'Rating': rating_list
        }
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = "flipkart.csv"
df.to_csv(csv_file_path, index=False, encoding='utf-8', mode='a')

print("Data scraping completed and saved to", csv_file_path)

