n = int(input("entrer la taille de votre pattern: "))
print(" "*(n)+"x")
for i in range(1,n):
    print(" "*(n-i)+"x"+" "*(2*i-1) + "x" )
    if i== n-1:
        print("x"*(n-(n//2)+1)+" "*(n-1)+"x"*(n-(n//2)+1))
for i in range(1,n-1):
    print(" "*(n-(n//2))+"x"+" "*(n-1)+"x")
    if i == n-2:
        print(" "*(n-(n//2))+"x"*(n+1))