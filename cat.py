!/usr/bin/python3
options='''
1.Cat 
2.Cat for multiple files
3.number of lines with file
4.Show $ in end of every line
'''
print(options)
choice=input("Enter the number:")

if choice == '1' :
        a=input("Enter the file:")
        f = open(a,'r')
        print(f.read())
        f.close()

elif choice == '2' :
        n=int(input("Enter number of files:"))
        file1=[]
        print("Enter name of files:")
        for i in range(1,n+1) :
                fname=input()
                file1.append(fname)
         for i in file1 :
                f=open(i,'r')
                print(f.read())
                f.close()

elif choice == '3' :
        file3 = input("Enter name of file:")
        with open(file3) as fp :
            line = fp.readline()
            cnt=1
            while line :
                print("Line {}: {}".format(cnt,line.strip()))
                line = fp.readline()
                cnt += 1

elif choice == '4' :
        file4 = input("Enter name of file:")
        f=open(file4,'r')
        data=f.read()
        splt=data.split("\n")
        for i in splt :
                print(i + "$")
                                    
