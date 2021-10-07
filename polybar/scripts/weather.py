import requests
import os
from dotenv import load_dotenv
load_dotenv()

CITY="1261039"
# set your openweathermap api key 
API_KEY = os.environ.get("API_KEY")
UNITS="metric"
UNIT_KEY="C"
LANG="en"

REQ = requests.get(f"http://api.openweathermap.org/data/2.5/weather?id={CITY}&appid={API_KEY}&units={UNITS}&lang={LANG}")

try:
    if(REQ.status_code == 200):
        DATA = REQ.json()
        CURRENT = DATA["weather"][0]["description"].capitalize()
        TEMP = float(DATA["main"]["temp"])
        FEELS_LIKE = float(DATA["main"]["feels_like"])
        NAME = DATA["name"]
        print(f"{NAME}, {CURRENT} {TEMP}°{UNIT_KEY} feels like {FEELS_LIKE}°{UNIT_KEY}")
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except(ValueError, IOError):
    print("Error: Unable to print the data")