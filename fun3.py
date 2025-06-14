#2.keyword arguments example program

#Method1

def sub(n1,n2):
    print(n1-n2)

sub(n1=15,n2=6)
sub(n2=6,n1=15)

#Method2

def sub(n1,n2):
    return n1-n2

r1=sub(n1=15,n2=6)
r2=sub(n2=6,n1=15)

print(r1)
print(r2)