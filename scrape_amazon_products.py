import requests
from bs4 import BeautifulSoup

def scrape_amazon_products(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  products = []
  for product in soup.find_all("div", class_="s-result-item"):
    url = product.find("a", class_="a-link-normal").get("href")
    name = ""
    try:
      name = product.find("span", class_="a-size-base-plus a-color-base").text
    except:
      pass

    price = ""
    try:
      price = product.find("span", class_="a-price").text
    except:
      pass

    rating = product.find("span", class_="a-icon-star").text
    reviews = product.find("span", class_="a-size-base").text

    products.append({
      "url": url,
      "name": name,
      "price": price,
      "rating": rating,
      "reviews": reviews,
    })

  return products

products = scrape_amazon_products("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1")

for product in products:
  print(product)



def scrape_amazon_product_details(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  description = soup.find("div", class_="a-section a-expander-content").text
  asin = soup.find("span", class_="a-size-base a-color-secondary").text
  product_description = soup.find("div", class_="a-row a-spacing-small").text
  manufacturer = soup.find("span", class_="a-size-base").text

  return {
    "description": description,
    "asin": asin,
    "product_description": product_description,
    "manufacturer": manufacturer,
  }

product_details = scrape_amazon_product_details("https://www.amazon.in/dp/B08P98325G")

print(product_details)
