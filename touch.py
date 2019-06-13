#!/usr/bin/python3
import os
from datetime import datetime
import time
import sys
import tempfile
option='''
1.To make a file without opening it.
2.to not create a file if it does not exist.
3.to set current date and time with file.
4.create more than one file together.
'''
print(option)
choice=raw_input()

if choice == '1' :
        a=raw_input("Enter file name:")
        os.mknod(a)

#do not create a file if it does not exist
#touch -c filename
elif choice == '2' :
        b=raw_input("Enter the filename:")
        f=open(b,'r')

#to create a file with current date and time
#modification of time
elif choice == '3' :
        c=raw_input("Enter file name:")
        os.utime(c,None)  #how to input file from user?

elif choice == '4' :
        fi=open('a.txt','r')
        data=fi.read()
        splt=data.split('\n')
        for i in splt:
                f=open(i,'w') #it is making multiple files but showing error too

