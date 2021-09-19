n1=int(input("Enter the lower range: "))
n2=int(input("Enter the upper range: "))

print("Strong numbers are:")

for i in range(n1,n2+1):
    n=i
    s=0
    while(n>0):
        j,f=1,1
        rem=n%10
        for j in range(1,rem+1):
            f=f*j
        s=s+f
        n=n//10
    if(s==i):
        print(i,end=" ")