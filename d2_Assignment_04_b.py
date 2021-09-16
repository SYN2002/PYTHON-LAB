n=int(input("Enter the number: "))
n1=n2=n
i,r,rem,sum=0,0,0,0
while n1>0:
    r=r+1
    n1=n1//10
for i in range(0,n2):
    rem=n2%10
    sum = sum+ pow(rem,r)
    n2=n2//10
print(r)
print(rem)
print(sum)