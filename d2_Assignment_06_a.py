n=int(input("Enter the number: "))
sum,i=0,0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(n," is a perfect number!")
else:
    print(n," is a not perfect number!")