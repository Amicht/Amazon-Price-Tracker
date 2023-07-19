## Amazon Price Tracker

### Description
The Amazon Price Tracker Check a specific product in Amazon every day and alert the user by email, if the product's price is under the requested value.


### Instructions
In The 'main.py' file, set your own configuration:

    product_name, 
    min_price: the lowest price value in Dollars you are willing to pay,
    product_url: a link to the product in Amazon

And that is it!
The APT will take care of the rest.

### Resources And Libraries
- requests: server request
- smtplib: sending email
- BeautifulSoup: scrap from amazon
- python-dotenv: env file variables