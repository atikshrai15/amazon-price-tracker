import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import time

# add more amazon links by using "amazon_link" / "new_amazon_link"
URL = "https://www.amazon.com/Elgato-Stream-Deck-Mini-customizable/dp/B07DYRS1WH/ref=sr_1_3?crid=2NW868TSVTOFU&keywords=stream+deck+mini&qid=1688670886&s=electronics&sprefix=stream+deck+mini%2Celectronics%2C85&sr=1-3&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc"
headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-US,en;q=0.9',
}

page = ''
while page == '':
    try:
        response = requests.get(url=URL, headers=headers)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        time.sleep(5)
        continue

soup = BeautifulSoup(response.text, "lxml")

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)

YOUR_EMAIL = "atikshrai@gmail.com"
YOUR_PASSWORD = "twtmsmxdunfrehjg"

title = soup.find(id="productTitle").get_text().strip()

price_as_float = float(price)
# set the price you are willing to buy the item on
BUY_PRICE = 50

if price_as_float < BUY_PRICE:
    message = f"{title} is now \n${price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
