from product import ProductTracker


# product config
name = "LED Projector"
product_url = "https://www.amazon.com/-/he/%D7%95%D7%91%D7%9C%D7%95%D7%98%D7%95%D7%AA-%D7%97%D7%99%D7%A6%D7%95" \
   "%D7%A0%D7%99-13000L-V6-Keystone/dp/B08HLLQV1J/ref=sr_1_3?crid=3C7L4PB91XH4C&keywords=LED" \
   "+Projector&qid=1689721592&sprefix=led+projector%2Caps%2C205&sr=8-3"
min_price = 129


# start daily price check
product = ProductTracker(url=product_url, name=name, min_price=min_price)
product.start_price_check()


