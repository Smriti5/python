#!/usr/bin/python3
import webbrowser
import time
import subprocess
import os

option='''
1.To open a file
2.To open fav song in youtube
3.To search on google
4.To send message to fav whatsapp number
5.To print current date and time
6.To reboot
'''

print(option)

choice=input()

if choice == 1 :
        subprocess.call('gedit')

elif choice == 2 :
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=ixkoVwKQaJg')

elif choice == 3 :
        data=raw_input("Enter what you want to search:")
        webbrowser.open_new_tab('https://www.google.com/search?q='+data)
        
elif choice == 4 :
        d=raw_input("Enter the number:")
        webbrowser.open_new_tab('https://api.whatsapp.com/send?phone='+d)

elif choice == 5 :
        current_time=time.ctime()
        print(current_time)

elif choice == 6 :
        os.system('reboot')

else:
        print("hi")
                         
