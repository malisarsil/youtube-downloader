# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:10:52 2020

@author: sarsi
"""
# Inputting a word relevant to the song you want to listen
# and downloading the first song in youtube search

from youtube_search import YoutubeSearch
import json
import os

search = str(input("please enter what you want to listen to: "))

results_list = YoutubeSearch(search, max_results = 3).to_json()
exact = json.loads(results_list)
url = "https://www.youtube.com"
url = url + exact["videos"][0] ["url_suffix"]

print(url)

#the path where to be downloaded

path = "C:\\Users\\sarsi\\Desktop"

from pytube import YouTube
import pytube
import os
name = pytube.extract.video_id(url)
YouTube(url).streams.filter(only_audio=True).first().download(filename=name)
location = path + name + '.mp4'
renametomp3 = path + name + '.mp3'
os.system('ren {0} {1}'. format(location, renametomp3))



