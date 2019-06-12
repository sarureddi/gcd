g1=input()
g1=g1.split()
a=int(g1[0])
b=int(g1[1])
i=1
while(i<=a and i<=b):
    if((a%i==0) and (b%i==0)):
        gcd=i
    i=i+1
print(gcd)
