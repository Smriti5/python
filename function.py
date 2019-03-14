#! /usr/bin/python
a=int(input("enter a no:"))
b=int(input("enter a no:"))
print("1=Add,2=Sub,3=Multiply,4=Divide,5=table of first input")
c=int(input("enter a no from 1 to 5:"))

def operations(c):

	if c == 1:
		print(a + b)
	if c == 2:
		 print(a - b)
	if c == 3:
		 print(a * b)
	if c == 4:
		 print(a / b)
	if c == 5:
		for e in range(1,11):
			print(a * e)

operations(c)
