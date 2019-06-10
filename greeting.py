#!/usr/bin/python3

import datetime
a=datetime.datetime.now()

if 6 <= a.hour < 12 :
        print("Good morning")

elif 12 <= a.hour <16 :
        print("Good afternoon")

elif 16 <= a.hour <20 :
        print("Good evening")

else :
        print("Good Night")
