import random
import smtplib

import pandas as pd
import datetime as d
import main as m

##################### Extra Hard Starting Project ######################


def send_mail(to, message):
    connection = smtplib.SMTP()
    connection.connect(host=m.host)
    connection.starttls()
    connection.login(user=m.email, password=m.password)
    connection.sendmail(from_addr=m.email, to_addrs=to, msg=message)
    connection.close()


# 1. Update the birthdays.csv

birthday = {
    "name": ["today", "jon", "jane"],
    "email": ["today@toot.com", "jon@jon.com", "jean@do.com"],
    "year": [2023, 1959, 1992],
    "month": [4, 10, 5],
    "day": [8, 6, 2],
}

letters = [
    "./templates/letter_1.txt",
    "./templates/letter_2.txt",
    "./templates/letter_3.txt",
]

# pd.DataFrame(birthday).to_csv("birthdays.csv", index=False)
data = pd.read_csv("./birthdays.csv")
new_data = data.values


# 2. Check if today matches a birthday in the birthdays.csv
today_day = d.datetime.now().day
today_month = d.datetime.now().month
new_letter = ""
for i in new_data:
    if today_day in i and today_month in i:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        to_mail = i[1]
        with open(random.choice(letters)) as letter:
            letter_temp = letter.read()
            new_letter = letter_temp.replace("[NAME]", i[0], 1)
        send_mail(to_mail, new_letter)
        print(to_mail, new_letter)


# 4. Send the letter generated in step 3 to that person's email address.
