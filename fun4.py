#3.default arguments example program

#Method1

def mul(a,b,c=2):
    print(a*b*c)

mul(2,3,4)
mul(2,3)

#Method2

def mul(a,b,c=2):
    return a*b*c

r1=mul(2,3,4)
r2=mul(2,3)
print(r1)
print(r2)

#Method2

def add(a,b):
    return a-b

sub1=add(a=10,b=20)
sub2=add(b=20,a=10)    
print(sub1)
print(sub2)
