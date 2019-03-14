#! /usr/bin/python

def table(n):
	return lambda x: x+n

n=int(input("enter no:"))

b=table(n)
a=0

for i in range(0,5):
	print(b(a))
	a=a+10
