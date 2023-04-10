import smtplib

import requests
from datetime import datetime
import day32.main as mail
import config as c
import time

response = requests.get(url=c.ISS_API_URL)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": c.MY_LAT,
    "lng": c.MY_LONG,
    "formatted": 0,
}

response = requests.get(c.SUN_API_URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# If the ISS is close to my current position
# and it is currently dark
def is_iss_close(iss_lat, iss_lang, s_r, s_s):
    limit = 5
    diff_lat = abs(c.MY_LAT - iss_lat)
    diff_lng = abs(c.MY_LONG - iss_lang)
    if diff_lng <= limit and diff_lat <= limit:
        if s_r >= time_now.hour >= s_s:
            return True
    else:
        return False


message = """Look up, my friend! The International Space Station is currently orbiting overhead, traveling at a speed of approximately 28,000 kilometers per hour. From its vantage point 400 kilometers above the Earth, the ISS offers a breathtaking view of our planet, reminding us of the beauty and fragility of our home in the vastness of space. Take a moment to appreciate this awe-inspiring sight and reflect on our place in the universe.
"""
is_close = is_iss_close(iss_latitude, iss_longitude, sunrise, sunset)


# Then send me an email to tell me to look up.
def send_mail(msg):
    connection = smtplib.SMTP()
    connection.connect(host=mail.host)
    connection.starttls()
    connection.login(user=mail.email, password=mail.password)
    connection.sendmail(from_addr=mail.email, to_addrs=mail.to_addrs, msg=msg)
    connection.close()


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_close:
        send_mail(message)
        print(message)
