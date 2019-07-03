#coding:utf-8
import urllib2
import time
from datetime import datetime
from bs4 import BeautifulSoup

# main page http://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx
# cinama 1:信義威秀 cinema=1|TP 2:京站威秀 cinema=12|QS
quote_page = 'http://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx?cinema=1|TP&movie=HO00008000'

def get_1stday_section():
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    # for Marvel studio, always find the first release day.
    movie_day_list = soup.find("div", {"class": "movieDay"})
    #movieDay = soup.find('movieDay')

    time_list = movie_day_list.find_all('li')
    #print movie_day_list
    return movie_day_list, len(time_list)

def get_section(round):
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    # for spiderman far from home, find the second day.
    movie_day_list = soup.find_all("div", {"class": "movieDay"})
    movie_day_list = movie_day_list[round]
    time_list = movie_day_list.find_all('li')

    #print movie_day_list
    return movie_day_list, len(time_list)

# beside the Pre-sale ticket already release one week earlier, we assume there might have other time will release later, count the total number bigger than.

if __name__ == "__main__":
    movie_day_list, new_time_list_count = get_section(1)
    print(movie_day_list)
    # trigger_count means the current pre-sale sessions, count by html "li" attribute.
    trigger_count = 13
    print("Bias: {}".format(str(trigger_count)))
    while True:
        movie_day_list, new_time_list_count = get_section(1)
        if trigger_count < new_time_list_count:
            print("New Schedule!\a")
            for i in range(20):
                print("Go! Go! count: {}, {} \a".format(str(i), str(datetime.now())))
                time.sleep(1)
            continue
        else:
            #print("No new Schedule.")
            pass
        time.sleep(30)

