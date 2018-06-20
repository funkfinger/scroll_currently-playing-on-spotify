#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse
import pylast

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from config import *

import urllib2
import time;

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)


def show_time():
    import time;
    t = time.localtime(time.time())
    time_string = time.strftime(" * %a, %b %d - %I:%M * ", t)
    show_message(device, time_string, fill="white", font=proportional(LCD_FONT))


def now_playing():
    response = urllib2.urlopen('https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=' + LASTFM_API_USER + '&api_key=' + LASTFM_API_KEY + '&limit=1')
    html = response.read()
    udata=html.decode("utf-8")
    asciidata=udata.encode("ascii","ignore")

    import xml.etree.ElementTree as ET
    tree = ET.fromstring(asciidata)

    artist = tree.find('artist')

    artist = "unknown"
    track = "unknown"

    for elem in tree.iter():
        if elem.tag == 'artist':
            if artist == "unknown": artist = elem.text
            if artist is None: artist = "???"
        if elem.tag == 'name':
            if track == "unknown": track = elem.text
            if track is None: track = "???"

    msg = "" + artist + " - " + track
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def scroller():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

    # start demo
    msg = "NOW PLAYING: "
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def getIP():
# 	import socket
# 	ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
	ip = 'Royce & Amy'
	return ip


if __name__ == "__main__":
    try:
#         show_message(device, "WELCOME" + str(getIP()) + "!", fill="white", font=proportional(CP437_FONT))
        show_message(device, "WELCOME!", fill="white", font=proportional(CP437_FONT))
        time.sleep(1)
        while(1):
            show_time()
            now_playing()
            time.sleep(5)
    except Exception:
        print("error but trudging on...")
        pass
