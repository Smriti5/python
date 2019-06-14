#!/usr/bin/python36

import os

def check(a):
         return os.system(a+'&> /dev/null &')

for i in range(1,11):
        a=raw_input("Enter the command:  ")
        y=check(a)
        if y == 0 :
                b=raw_input("Enter data:")
                os.system(a+" "+b)

        else :
                os.system('echo error | festival --tts')
