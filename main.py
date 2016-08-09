#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import texttable as tt
ID=sys.argv[1]
LANG=sys.argv[2]
URL="https://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang={}&idc={}".format(LANG, ID)

r = requests.get(URL)

soup = BeautifulSoup(r.text, "lxml")
status_div = soup.find("div", { "class" : "well well-status" })
date = status_div.find("h2").get_text()
date = date.split(' ', 2)[2]
status = status_div.find("p").get_text()

tab = tt.Texttable()
tab.header(['ID', 'Date', 'State'])
tab.set_cols_dtype(['i', 't', 't'])
row = [str(ID), date, status]
tab.add_row(row)
tab.set_cols_width([15, 20, 50])
tab.set_cols_align(['c','c','l'])
tab.set_deco(tab.HEADER | tab.VLINES)

print(tab.draw())
