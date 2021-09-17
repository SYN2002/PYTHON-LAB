n=int(input("Enter the upper limit: "))
a,b=0,1
sum,i= 0,0
for i in range(1,n+1):
    if sum<=n:
        print(sum,end=" ")
    a=b
    b=sum
    sum= a+b