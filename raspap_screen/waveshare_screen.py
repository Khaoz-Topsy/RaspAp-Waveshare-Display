#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import requests
import logging
from waveshare_epd import epd2in13b_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
base_api_url = "http://127.0.0.1:8081/"
client_ap_name = "wlan1"
auth_headers = {'access_token': ''}

try:
    logging.info("Kurt's custom screen")

    epd = epd2in13b_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
    emptyImage = Image.new('1', (epd.width, epd.height), 255)

#    logging.info("Drawing loading screen")
#    loadingImage = Image.new('1', (epd.height, epd.width), 255)
#    loadingDraw = ImageDraw.Draw(loadingImage)
#    loadingDraw.text((5, 0), 'Loading', font = font18, fill = 0)
#    loadingDraw.line((0, 25, epd.height, 25), fill = 0)
#    loadingImage = loadingImage.transpose(Image.ROTATE_180)
#    epd.display(epd.getbuffer(loadingImage), epd.getbuffer(emptyImage))

    systemResponse = requests.get(base_api_url + "system", headers=auth_headers)
    systemJson = systemResponse.json()

    apResponse = requests.get(base_api_url + "ap", headers=auth_headers)
    apJson = apResponse.json()

    clientsResponse = requests.get(base_api_url + "clients/" + client_ap_name, headers=auth_headers)
    clientsJson = apResponse.json()

    infoImage = Image.new('1', (epd.height, epd.width), 255)
    infoDraw = ImageDraw.Draw(infoImage)
    infoDraw.text((5, 0), systemJson.get('hostname'), font = font18, fill = 0)
    infoDraw.text((epd.height - 50, 0), time.strftime('%H:%M'), font = font18, fill = 0)
    infoDraw.line((0, 25, epd.height, 25), fill = 0)
    infoDraw.text((5, 30), "SSID: " + apJson.get('ssid'), font = font12, fill = 0)
    infoDraw.text((5, 45), "Num Clients: " + str(clientsJson.get('active_clients_amount')), font = font12, fill >    infoDraw.text((5, 60), "Uptime: " + systemJson.get('uptime'), font = font12, fill = 0)
    infoDraw.text((5, 75), "Temp °C: " + str(systemJson.get('systemTemperature')), font = font12, fill = 0)
    infoImage = infoImage.transpose(Image.ROTATE_180)
    epd.display(epd.getbuffer(infoImage), epd.getbuffer(emptyImage))

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13b_V4.epdconfig.module_exit(cleanup=True)
    exit()
