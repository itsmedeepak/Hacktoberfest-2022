"""import smtplib

MY_EMAIL = "rst00711@gmail.com"
PASS = "Cre01b@8804"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

connection.login(user=MY_EMAIL, password=PASS)
connection.sendmail(from_addr=MY_EMAIL, to_addrs="deepak8804375275@gmail.com", msg="hello")
connection.quit()"""

# Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "rst00711@gmail.com"
ANOTHER = "deepak8804375275@gmail.com"
MY_PASSWORD = "Cre01b@8804"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=ANOTHER,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
        print(f"Sent successfully to {ANOTHER}")
