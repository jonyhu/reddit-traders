# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:58:44 2020

@author: Jonathan Hu

"""

import praw
import requests


headers = {"Authorization": "bearer 480541324040-IFlDm5jyUOIlzkN1pcOY6XMP9ng", "User-Agent": "ec980z/0.1 by MeanderingMeribah"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
response = requests.get("https://oauth.reddit.com/r/WallStreetBets/about", headers=headers)
response.json()
