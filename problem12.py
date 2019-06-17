#!/usr/bin/python3
import os
import pyqrcode
from pyqrcode import QRCode
from googlesearch import search

url=[]
b=1
a=input("Enter your search:")
for i in search(a,stop=3):
        url.append(i)
        img1=pyqrcode.create(i)
        img1.svg("qr"+str(b)+".svg",scale=6)
        b+=1
        print(img1)
        
fi=input("Enter the html file:")
os.system("touch"+" "+fi)
os.system('echo "<html><h1>QR Code for search:n </h1><body><img src="qr1.svg"><img src="qr2.svg"><img src="qr3.svg"></body</html>"'+fi)
os.system('sudo mv qr1.svg /var/www/html/')
os.system('sudo mv qr2.svg /var/www/html/')
os.system('sudo mv qr3.svg /var/www/html/')
