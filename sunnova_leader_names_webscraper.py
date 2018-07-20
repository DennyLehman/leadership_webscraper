# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:44:38 2018

@author: Denny.Lehman
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def get_leadership():
    # select url
    my_url = 'https://www.sunnova.com/leadership-team/'

    # open connection
    uClient = uReq(my_url)

    # copy the html
    page_html = uClient.read()

    # close the connection
    uClient.close()

    # makes the beautiful soup
    page_soup = soup(page_html, 'html.parser')

    page_soup.body.div.section.div.div.div

    containers = page_soup.find_all("div", {"class": "small-12 medium-6 large-8 columns"})
    leader_name_list = []
    if len(containers) > 0:
        print('The leadership team at Sunnova is: ')
        for container in containers:
            leader_name = container.h2.text
            leader_name_list.append(leader_name)
            #print(leader_name)

    return leader_name_list

if __name__ == '__main__':
    print('Hello world, in name = main')
    print(get_leadership())
