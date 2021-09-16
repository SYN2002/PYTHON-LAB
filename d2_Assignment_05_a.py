n=int(input("Enter the number: "))
n2=n
sum=0
while (n2>0):
    f=1
    i=1
    rem=n2%10
    while (i<=rem):
        f=f*i
        i=i+1
    sum=sum+f
    n2=n2//10
if(sum==n):
    print("The given number is an strong number!")
else:
    print("The given number is not an strong number!")