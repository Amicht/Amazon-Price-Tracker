from bs4 import BeautifulSoup as Bs
from requests import HTTPError, get
from requests.exceptions import InvalidURL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7"
}


def get_product_price(product_url: str) -> None | int:
    try:
        amazon_response = get(product_url, headers=headers)
        amazon_response.raise_for_status()
        soup = Bs(amazon_response.text, "html.parser")
    except:
        return None
    else:
        price_tag = soup.find(name="span", class_="a-price-whole")
        if not price_tag:
            return None
        price = price_tag.getText().replace(".", "").replace("\"", "").replace("\u200e", "").strip()
        return int(price)
