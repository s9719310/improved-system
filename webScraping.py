import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.digikala.com/search/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D9%85%D9%88%D8%A8%D8%A7% DB%8C%D9%84"
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the mobile phone containers on the page
mobile_containers = soup.find_all("div", {"class": "product-list_ProductList__item__LiiNI" , {"data-product-index" : "49"}})
print('url',url)
print('response',response)
print('soup',soup)
print('mobile_containers',mobile_containers)
# Iterate over each mobile phone container and extract the name and price
for mobile in mobile_containers:
    # Extract the name of the mobile phone
    name = mobile.find("div", {"class": "c-product-box__title"}).text.strip()

    # Extract the price of the mobile phone
    price = mobile.find("div", {"class": "c-price__value"}).text.strip()

    # Print the mobile phone name and price
    print("Mobile Phone Name:", name)
    print("Price:", price)
    print("--------------------")
