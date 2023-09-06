#!/usr/bin/env python3

import requests

from bs4 import BeautifulSoup
from library.lcd.lcd_comm_rev_b import LcdCommRevB, Orientation

# init LCD
lcd=LcdCommRevB()  # default is AUTO,320,480
lcd.Reset()  # Does nothing for Rev B hardware
lcd.InitializeComm()
lcd.SetOrientation(Orientation.LANDSCAPE)
lcd.SetBrightness(10);

# background graphic
back='had.png'
lcd.DisplayBitmap(back)

# scrape
r=requests.get('http://www.hackaday.com')
if (r.ok) :
    soup=BeautifulSoup(r.content,'html.parser')
    entry=soup.find('div',class_='entry-intro')
    title=entry.findAll('a')[1].text;
# put title on LCD
    print(f"Found {title}\n")
    lcd.DisplayText(" " + title,0,280,font_size=16,font_color=(0,0,0),background_color=(255,255,255))
    exit(0)
else :  # error message
    lcd.DisplayText(" Internet error!",0,280,font_size=16,font_color=(0,0,0),background_color=(255,255,255))
exit(1)    
