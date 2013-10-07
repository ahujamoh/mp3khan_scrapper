#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import requests

site = 'http://mp3khan.net/'
latest_flag = 1
latest_dict = {}
indian_movie_dict = {}
temp1 = {}
temp2 = {}

def prompt():
    return initialize(raw_input("Enter Your choice: "))

def indian_movie_songs(url):
    response = requests.get(site + url)
    soup = BeautifulSoup(response.text)
    del response
    if latest_flag == 1:
        print "Showing latest songs:"
        for latest in soup.findAll('td', attrs={'width' : '57%'}):
            for link in latest.findAll('a'):
                latest_dict[link.text] = site + link.get('href')
        counter = 1
        for key in latest_dict.keys():
            print str(counter) + ". " + (' ').join(key.split())
            temp1[counter] = key
            counter += 1
    for song in soup.findAll('td', attrs={'width' : '50%'}):
        for link in song.findAll('a'):
            indian_movie_dict[link.text] = site + link.get('href')
    counter = 1
    print "Showing all songs:"
    for key in indian_movie_dict.keys():
        print str(counter) + ". " + (' ').join(key.split())
        temp1[counter] = key
        counter += 1

def initialize(choice):
    print "Scrapping started...\nTarget: mp3khan.net\n"
    url_dict = {
        "1" : "indian-movies-songs.html",
        "2" : "EnglishPopPage.html",
        "3" : "single-tracks.html",
        "4" : "indian-pop-songs.html",
        "5" : "uk-bhangra.html"
        }
    try:
        return url_dict[choice]
    except:
        print "Are you kidding? Enter choice correctly"
        prompt()

if __name__ == '__main__':
    print "1. Bollywood Movie Songs"
    print "2. English Pop Songs/Albums"
    print "3. ExclusivE Single Tracks"
    print "4. Indian Pop / Remixes"
    print "5. UK Bhangra Punjabi Albums"
    songs = prompt()
    indian_movie_songs(songs)

# td width="57%" for latest addition
# <td width="50%" align="left" valign="top" id="border_both" style="padding:0 10px 0 10px;">
#<a href="1920_evil_returns_2012_mp3_movie_songs_download.html">
#							1920 Evil Returns (2012)</a><br />
#<a href="3g_2013_mp3_movie_songs_download.html"><b>

