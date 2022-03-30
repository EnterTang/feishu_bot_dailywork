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

# 通知服务
# BARK = ''                   # bark服务,自行搜索; secrets可填;
# BARK_PUSH=''                # bark自建服务器，要填完整链接，结尾的/不要
# SCKEY = ''                  # Server酱的SCKEY; secrets可填
# TG_BOT_TOKEN = ''           # tg机器人的TG_BOT_TOKEN; secrets可填1407203283:AAG9rt-6RDaaX0HBLZQq0laNOh898iFYaRQ
# TG_USER_ID = ''             # tg机器人的TG_USER_ID; secrets可填 1434078534
# TG_API_HOST=''              # tg 代理api
# TG_PROXY_IP = ''            # tg机器人的TG_PROXY_IP; secrets可填
# TG_PROXY_PORT = ''          # tg机器人的TG_PROXY_PORT; secrets可填
# DD_BOT_ACCESS_TOKEN = ''    # 钉钉机器人的DD_BOT_ACCESS_TOKEN; secrets可填
# DD_BOT_SECRET = ''          # 钉钉机器人的DD_BOT_SECRET; secrets可填
# QQ_SKEY = ''                # qq机器人的QQ_SKEY; secrets可填
# QQ_MODE = ''                # qq机器人的QQ_MODE; secrets可填
# QYWX_AM = ''                # 企业微信
# QYWX_KEY = ''                # 企业微信BOT
# PUSH_PLUS_TOKEN = ''        # 微信推送Plus+
FEISHU_BOT_URL = 'http://101.34.179.196:8000/qinglong/send'
FEISHU_BOT_CHATID = 'oc_3f2b44fa0291318092e42d86f4b886a2'

notify_mode = []

message_info = ''''''

if "FEISHU_BOT_URL" in os.environ and os.environ["FEISHU_BOT_URL"]:
    FEISHU_BOT_URL = os.environ["FEISHU_BOT_URL"]
if "FEISHU_BOT_CHATID" in os.environ and os.environ["FEISHU_BOT_CHATID"]:
    FEISHU_BOT_CHATID = os.environ["FEISHU_BOT_CHATID"]

if FEISHU_BOT_URL:
    notify_mode.append('feishu')

def message(str_msg):
    global message_info
    print(str_msg)
    message_info = "{}\n{}".format(message_info, str_msg)
    sys.stdout.flush()

def feishu_bot(content):
    payload = {'send_to':FEISHU_BOT_CHATID, 'msg_send':content}
    if FEISHU_BOT_URL and FEISHU_BOT_CHATID:
        try:
            response = requests.post(url=FEISHU_BOT_URL, data=json.dumps(payload)).json()
            print(response)
        except:
            print('推送失败！')


def send(content):
    for i in notify_mode:
        if i == 'feishu':
            if FEISHU_BOT_URL and FEISHU_BOT_CHATID:
                feishu_bot(content)