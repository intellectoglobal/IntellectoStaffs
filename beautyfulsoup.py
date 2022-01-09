from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup

try:
    stock_symbol = "AMZN"
    stock_url = "https://finance.yahoo.com/quote/" + stock_symbol
    print(stock_url)

    res = requests.get(stock_url)

    soup = BeautifulSoup(res.text, 'html.parser')

    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('span')[0].text
    change = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('span')[1].text

    print(price, change)

except Exception:
    print("Invalied Input")


# price = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
# change = soup.find('span', {'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"}).text
# print(price, change)


# data_array = soup.find(id='responsiveDiv').getText().strip().split(":")
# type (data_array)


# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)