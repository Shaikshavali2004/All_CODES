# Argument Types:

#1.positional arguments
#2.keyword arguments
#3.default arguments
#4.Variable Length Arguments

#1.positional arguments example program.

#Method1

def sub(a,b):
    return a-b

r1=sub(10,35)
r2=sub(35,10)
print(r1)
print(r2)

#Method2

def sub(a,b):
    print(a-b)

sub(10,35)
sub(35,10)