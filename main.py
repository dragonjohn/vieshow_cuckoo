#coding:utf-8
import urllib2
import time
from bs4 import BeautifulSoup

# main page http://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx
# cinama 1:信義威秀 cinema=1|TP 2:京站威秀 cinema=12|QS
quote_page = 'http://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx?cinema=1|TP&movie=HO00008000'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

# for Marvel studio, always find the first release day.
movie_day_list = soup.find("div", {"class": "movieDay"})
#movieDay = soup.find('movieDay')


# for spiderman far from home, find the second day.
movie_day_list = soup.find_all("div", {"class": "movieDay"})
movie_day_list = movie_day_list[1]
time_list = movie_day_list.find_all('li')

print movie_day_list
print len(time_list)

# beside the Pre-sale ticket already release one week earlier, we assume there might have other time will release later, count the total number bigger than.

# trigger_count means the current pre-sale sessions, count by html "li" attribute.
trigger_count = 13
while True:
    if trigger_count < len(time_list):
	print("New Schedule!\a")
    else:
        #print("No new Schedule.")
        pass
    time.sleep(1)

