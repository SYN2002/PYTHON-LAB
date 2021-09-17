n1=int(input("Enter the lower limit: "))
n2=int(input("Enter the uper limit: "))
i,s=n1,0
print("Numbers are: ")
for i in range(n1,n2+1):
    j=i
    c,k=0,0
    while(j>0):
        c=c+1
        j=j//10
    for k in range(0,c):
        r=i%10
        s=s+r**c
        i=i//10