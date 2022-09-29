from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://novelkeys.com/collections/keycaps"
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class":"grid-view-item product-card"})

#opens excel file
filename = "products.csv"

f = open(filename, "w")

headers = "Product Name, Keycap Type, Price\n"

f.write(headers)

#parses through all containers on webpage and writes them to file
for container in containers:
    product_name = container.a.text.strip()

    details_container = container.find("div", {"class":"product-card-details-grid"})

    keycap_type = details_container.div.find("div", {"class":"h4 grid-view-item__title product-card__subtitle"}).text.strip()

    price = details_container.find("div", {"class":"price-item price price__regular price-item--regular"})

    if (price.span.text != "\n"):
        product_price = price.span.text.strip()
    else:
        product_price = price.text.strip()

    f.write(product_name + "," + keycap_type + "," + product_price + "\n")

#closes file
f.close()