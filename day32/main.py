import smtplib

#
host = "smtp.milk.com"
email = "black@milk.com"
password = "milkybar100"
to_addrs = "white@milk.com"
# connection = smtplib.SMTP(host = host, port = 2892)
# connection.starttls()
# connection.login(user = email, password = "milkybar100")
# connection.sendmail(from_addr = email, to_addrs = "white@milk.com", msg = 'hello')
# connection.close()

import datetime as date

# print(date.datetime.now())
now = date.datetime.now()
# print(now.day)
# print(now.year)
# print(now.weekday())

dob = date.datetime(year=2050, month=10, day=1)
# print(dob)
