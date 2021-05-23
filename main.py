import datetime as dt
import smtplib
import random
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

now = dt.datetime.now()
now_week_day = now.weekday()

# day 0 is monday

if now_week_day == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()

    random_quote = random.choice(quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Motivation Quote\n\n{random_quote}"
        )
