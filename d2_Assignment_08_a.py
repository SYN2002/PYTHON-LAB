n1=int(input("Enter the lower limit: "))
n2=int(input("Enter the uper limit: "))
i,s=n1,0
c=0
print("Numbers are: ")
while i<=n2:
    j=k=i
    c=0
    while(j>0):
        c=c+1
        j=j//10
    s=0
    while k>0:
        r=k%10
        s=s+r**c
        k=k//10
    if(s==i):
        print(i)
    i=i+1