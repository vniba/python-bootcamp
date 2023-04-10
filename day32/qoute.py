import main as m
import datetime as date
import random
import smtplib

d = date.datetime.now().strftime("%A")
with open("./quotes.txt") as q:
    data = q.readlines()
mail = random.choice(data)
send = f"{d} Quotes \n {mail}"


def send_mail():
    connect = smtplib.SMTP()
    connect.connect(host=m.host)
    connect.starttls()
    connect.login(user=m.email, password=m.password)
    connect.sendmail(from_addr=m.email, to_addrs=m.to_addrs, msg=send)
    connect.close()


print("soda")
