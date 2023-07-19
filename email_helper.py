from email.message import EmailMessage
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.environ.get("PASSWORD")
MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_TO_SEND = os.environ.get("EMAIL_TO_SEND")


def send_email_alert(product_price: int, product_name: str, product_url: str):
    from_addr = MY_EMAIL
    to_addr = EMAIL_TO_SEND
    subject = f"Product Tracker Alert: {product_name} is now only ${product_price}!"

    first_line = f"The product you are intersted in,\n{product_name},"
    second_line = f"is now updated to only -\n${product_price}\n"
    final_line = f"Here is the link for purchase in amazon:\n{product_url}"
    content = f"{first_line}\n{second_line}\n{final_line}"

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = from_addr
    message['To'] = to_addr
    message.set_content(content)

    with SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(user=from_addr, password=PASSWORD)
        smtp.send_message(message)
        print("email send successfully!")
