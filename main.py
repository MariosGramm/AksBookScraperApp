import scraper
from config import default_category


menu = """
Welcome to the book-scraping app!
-----------------------------------
Here are the available categories:
"""

print(menu)

for key in scraper.links:
    print(key)

while True:
    category = input("Please choose a category: ")
    if category in scraper.links:
        break
    if category == "":
        category = default_category
        break
    else:
        print("Category does not exist.Please try again or leave blank.")



while True:
    try:
        price_min = int(input("Please choose the minimum price: "))
        if price_min < 0:
            print("Invalid price.Price cannot be negative. Please try again.")
            continue
    except ValueError:
        print("Invalid input.Please enter a valid number.")
        continue

    try:
        price_max = int(input("Please choose the maximum price: "))
        if price_max < 0:
            print("Invalid price.Price cannot be negative.Please try again.")
            continue
    except ValueError:
        print("Invalid input.Please enter a valid number.")
        continue

    if price_min > price_max:
        print("Minimum price cannot be higher than the maximum price.Please try again.")
        continue

    break


scraper.scrape(category, price_min , price_max) 
