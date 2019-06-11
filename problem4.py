import os
uname=raw_input("Enter username:")

def addnewuser():
        upass="hello"+uname
        os.system("useradd -m -p "+ upass +" "+uname)

if uname.isalpha():
        addnewuser()
        print("user is added")

else :
        print("error")
                       
