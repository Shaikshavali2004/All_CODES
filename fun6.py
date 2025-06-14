# def add():
#     print("hello world")
# add()

# def add(a,b):
#     return a+b
# r1=add("5","world")
# print(r1)

# def add(a,b=5):
#     print(a+b)

# add(1,2)
# add(6)

# def add(a,b,c=5):

#     return a+b-c
# r1=add(a=10,b=30)
# print(r1)
# r2=add(b=30,a=10,c=5)
# print(r2)

def num(a,p,*k):
    print("a:",a,"p:",p,"k:",k)

num(10,20,30)
num(19,28,27,283,83,383)