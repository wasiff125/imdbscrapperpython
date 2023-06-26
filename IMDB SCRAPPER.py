import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
import csv

# changing ther link
# https://www.imdb.com/search/title/?title_type=feature&genres=action&start=50&explore=genres&ref_=adv_nxt
# break the link into two parts like given below

imdb_url = "https://www.imdb.com/search/title/?title_type=feature&genres=action&start="
imdb_url_end = "&explore=genres&ref_=adv_nxt"

start_page = 51
increment = 50
num_pages = 200 #number of pages beign scrapped
data = []
counter = 1

for i in range(num_pages):
    page_number = start_page + (i * increment)
    url = f"{imdb_url}{page_number}{imdb_url_end}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    titles = soup.find_all("h3", class_="lister-item-header")
    rating = soup.find_all("strong")
 
    for title in titles:
        title_text = title.find("a").text
        title_with_number = f"{counter}. {title_text}"
        counter += 1
        for rate in rating:
            price_text = rate.text
            
        data.append([title_with_number, price_text]) 
    
        print(title_with_number,"\nRATING:"+price_text+"\n")

filename = os.path.abspath("imdb_10k.csv")
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Rating"])
    writer.writerows(data)

print(f"Scraped data saved to {filename}.")
