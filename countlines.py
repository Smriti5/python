#!/usr/bin/python3

fname=input("Enter file name:")
num_lines=0
#Now the file is opened in read mode 
#With statement automatically closes the file after the program in executed
with open(fname,'r') as f:
        for line in f :
                num_lines+=1
print("Number of lines are ");
print(num_lines)
