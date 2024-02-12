#1ex
n=int(input("before: "))
for i in range(1,n+1):
    print(i**2,sep="/n")
#2ex
n=int(input("before: "))
for i in range(0,n+1):
    if i%2==0:
        print(i,sep="/n")
#3ex
n=int(input("before: "))
for i in range(0,n+1):
    if i%3==0 and i%4==0:
        print(i,sep="/n")
#4ex
a=int(input("from: "))
b=int(input("before: "))
for i in range(a,b):
    print(i**2,sep="/n")
#5ex
a=int(input("from: "))
for i in range(a,-1,-1):
    print(i,sep="/n")
    