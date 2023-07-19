## Amazon Price Tracker

### Description
The Amazon Price Tracker Check a specific product in Amazon every day and alert the user by email, if the product's price is under the requested value.


### Instructions
In The `main.py` file, set your own product configuration:

    product_name, 
    min_price: the lowest price value in Dollars you are willing to pay,
    product_url: a link to the product in Amazon

Create a `.env` file in the root folder and set your 
email (as the sender of the email), 
password (enabled from the security settings in your email account)
and the email you want to send the alert to (it can be the same email or not).

** NOTE: this app only supports gmail accounts **

The file should look something like this:

    MY_EMAIL=myemail@gmail.com
    PASSWORD=jfgkdjfgkjdghkdsfg
    EMAIL_TO_SEND=useremail@gmail.com


And that is it!
The APT will take care of the rest.

### Resources And Libraries
- requests: server request
- smtplib: sending email
- BeautifulSoup: scrap from amazon
- python-dotenv: env file variables