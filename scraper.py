from bs4 import BeautifulSoup
import requests
from config import user_agent , url


headers = {"User-Agent": user_agent }

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,"html.parser")

#Εύρεση link ανά κατηγορία βιβλίων

ul_tag_1 = soup.find("ul" , class_ = "nav nav-list")

ul_tag_2 = ul_tag_1.find("ul")

li_tag = ul_tag_2.find("li")

links = {li_tag.text.strip():li_tag.find("a").get("href") for li_tag in ul_tag_2.find_all("li")}

#Scrape το category που επέλεξε ο χρήστης

def scrape(category, price_min, price_max):
    if category in links:
        url = f"https://books.toscrape.com/{links[category]}"
        print(f"Scraping books from: {url} (Price range: {price_min} - {price_max})")

        #Scraping
        books_dict = {}
        ratings_dict = {
            "One"   : 1,
            "Two"   : 2,
            "Three" : 3,
            "Four"  : 4,
            "Five"  : 5
        }
        while True: #for pagination
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text,"html.parser")
            books = soup.find_all("article" , class_ ="product_pod")
            books_dict |= {
                book.find("h3").find("a").get("title"):{
                    "price"         : book.find("p", class_ = "price_color" ).text[1:],
                    "star_rating"   : str(ratings_dict[book.find("p").get("class")[1]])+"/5",
                    "availability"  : book.find("p", class_ = "availability").text.strip() 
                }
                for book in books if (float(book.find("p", class_ = "price_color" ).text[2:])> price_min) and (float(book.find("p", class_ = "price_color" ).text[2:]) < price_max)
            }
            next_button = soup.find("li" , class_ = "next")
            if next_button:
                url = f"https://books.toscrape.com/{links[category][:-11]}/{next_button.find("a").get("href")}"
            else:
                break
        for title,info in books_dict.items():
            print(title,"| Price:", info["price"],"| Star Rating:", info["star_rating"],"| Availability:", info["availability"])
    else:
        print("Invalid category.")


















