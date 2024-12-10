#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess

from bs4 import BeautifulSoup

# Globals
WEB = "https://www.instant-gaming.com/es/"
WEB = "https://www.instant-gaming.com/en/"
WEB2 = "http://www.instant-gaming.com/"
WEB3 = "https://www.wikipedia.org/"


def oferts():
    """ Return your global IP """
    # response = urlopen(WEB)
    # bs = BeautifulSoup(response.read(), "html.parser")
    # response.close()

    response = subprocess.check_output(["curl", WEB])
    bs = BeautifulSoup(response, "html.parser")

    # for link in bs.find_all("a"):
    #   print(link.get("href"))

    # promotions = bs.find("promotions-home-block")

    # promotions = bs.find("promotions-home-block")
    promotions = bs.find_all(class_='item force-badge')

    # print(promotions)

    for link in promotions.find_all(class_="title"):
        print("###########################")
        print(link)  # print(link.get("href"))

    # cad1 = str(WEB)
    # cad1 = cad1.split('id="promotions-home-block"')[1]
    # cad1 = cad1.split('h2')[1]
    # cad1 = cad1.split(' ')[4].split('<')[0]
    # return cad1

    """ 
    import requests
    from bs4 import BeautifulSoup
    
    
    # Collect and parse first page
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Pull all text from the BodyText div
    artist_name_list = soup.find(class_='BodyText')
    
    # Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')
    """


if __name__ == '__main__':
    oferts()
