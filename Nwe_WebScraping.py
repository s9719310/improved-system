import requests
from bs4 import BeautifulSoup
import time

def get_mobile_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    mobile_containers = soup.find_all("div", {"class": "product-list_ProductListitemLiiNI", "data-product-index": "49"})
    mobile_data = []

    for mobile in mobile_containers:
        name = mobile.find("div", {"class": "c-product-box__title"}).text.strip()
        price = mobile.find("div", {"class": "c-price__value"}).text.strip()
        mobile_data.append((name, price))

    return mobile_data


if name == 'main':
    url = "https://www.digikala.com/search/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D9%85%D9%88%D8%A8%D8%A7% DB%8C%D9%84"
    start_time = time.time()
    mobile_data = get_mobile_data(url)
    end_time = time.time()
    execution_time = end_time - start_time

    for name, price in mobile_data:
        print("Mobile Phone Name:", name)
        print("Price:", price)
        print("--------------------")

    print("Execution Time (Serial):", execution_time)


Multithreading version:

python
import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

def get_mobile_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    mobile_containers = soup.find_all("div", {"class": "product-list_ProductListitemLiiNI", "data-product-index": "49"})
    mobile_data = []

    for mobile in mobile_containers:
        name = mobile.find("div", {"class": "c-product-box__title"}).text.strip()
        price = mobile.find("div", {"class": "c-price__value"}).text.strip()
        mobile_data.append((name, price))

    return mobile_data


def main_multithreaded():
    url = "https://www.digikala.com/search/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D9%85%D9%88%D8%A8%D8%A7% DB%8C%D9%84"
    with ThreadPoolExecutor() as executor:
        future = executor.submit(get_mobile_data, url)
        mobile_data = future.result()

    return mobile_data


if name == 'main':
    start_time = time.time()
    mobile_data = main_multithreaded()
    end_time = time.time()
    execution_time = end_time - start_time

    for name, price in mobile_data:
        print("Mobile Phone Name:", name)
        print("Price:", price)
        print("--------------------")

    print("Execution Time (Multithreading):", execution_time)
