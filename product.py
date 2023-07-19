from amazon_helper import get_product_price
from email_helper import send_email_alert


class ProductTracker:

    def __init__(self, url: str, min_price: int, name: str):
        self.url = url
        self.name = name
        self.min_price = min_price

    def start_price_check(self):
        current_price = get_product_price(self.url)

        if not current_price:
            print("Oops... failed to get Price from Amazon.")
            return

        if current_price <= self.min_price:
            send_email_alert(current_price, self.name, self.url)
        else:
            print(f"The current price ${current_price} is ${current_price - self.min_price} higher then your minimum "
                  f"price")