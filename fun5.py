#4.Variable Length Argumenst example program.

#Method1

def myfun(a,b,c,*d):
    return a,b,c,d

r1=myfun(10,30,10,40)
print(r1)
r2=myfun(10,30,10,30,40,50)
print(r2)

#Method2

def myfun(a,*b):
     print("a:",a,"and b:",b)

myfun(10,30,10,40)
myfun(10,30,10,30,40,50)