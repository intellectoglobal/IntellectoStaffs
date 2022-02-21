import requests
from bs4 import BeautifulSoup
#
i=('AAPL')
url =f"https://coinmarketcap.com/gainers-losers/"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
#
r = requests.get(url, header)
#
soup = BeautifulSoup(r.text, "html.parser")
#
price = soup.find('div', {'class' : 'sc'}).text
name = soup.find('div', {'class' : 'uikit-col-md-8 uikit-col-sm-16'}).text
# change = soup.find('span', {'class' : 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}).text

#x =
#
#
print(price)
