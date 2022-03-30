import sys
import os, re
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from datetime import date
import datetime

from etSendNotify import send

WEATHER_CITY = '杭州'
WEATHER_LOCATION_API = 'https://geoapi.qweather.com/v2/city/lookup?'
WEATHER_API = 'https://devapi.qweather.com/v7/weather/3d?'
WEATHER_KEY = 'fff9aa854a254e0fa452dd65725ae33b'

if "WEATHER_CITY" in os.environ and os.environ["WEATHER_CITY"]:
    WEATHER_CITY = os.environ["WEATHER_CITY"]
if "WEATHER_LOCATION_API" in os.environ and os.environ["WEATHER_LOCATION_API"]:
    WEATHER_LOCATION_API = os.environ["WEATHER_LOCATION_API"]
if "WEATHER_API" in os.environ and os.environ["WEATHER_API"]:
    WEATHER_API = os.environ["WEATHER_API"]

def getTodayInfo():
    weekdays = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
    today = date.today()
    result = "今日（" + str(today)[5:] + "）" + weekdays[datetime.datetime.now(tz=None).weekday() + 1] + "\n"
    return result
    # print("今日（{}）{}".format(str(today)[5:], weekdays[datetime.datetime.now(tz=None).weekday()]))

def getLocationCode():
    value = {
        "location":WEATHER_CITY,
        "key" : WEATHER_KEY
    }
    city_id = requests.get(WEATHER_LOCATION_API, params=value).json()["location"][0]["id"]
    return city_id

def getWeatherInfo(city_id):
    value = {
        "location":city_id,
        "key" : WEATHER_KEY
    }
    weather_info = requests.get(WEATHER_API, params=value).json()["daily"][0]
    result = "天气: " + weather_info["textDay"] + "\n"
    # print("天气:{}".format(weather_info["textDay"]))
    result = result + "温度: " + weather_info["tempMin"] + "~" + weather_info["tempMax"]
    return result
    # print("温度:{}~{}".format(weather_info["tempMin"], weather_info["tempMin"]))

result = getTodayInfo()
city_id = getLocationCode()
result = result + getWeatherInfo(city_id)

send(result)