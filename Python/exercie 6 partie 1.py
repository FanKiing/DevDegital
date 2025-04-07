#methode 1

a=1
b=0
c=a
a=b
b=c

print(a)
print(b)

#methode 2
a=0
b=1
a,b=(b,a)

print(a,b)
