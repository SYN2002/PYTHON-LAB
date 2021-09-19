n1=int(input("Enter the lower range: "))
n2=int(input("Enter the upper range: "))
print("Perfect numbers are:",end=" ")
if n1>0:
    for i in range(n1,n2+1):
        j,s=0,0
        for j in range(1,i):
            if(i%j==0):
                s=s+j
        if(s==i):
            print(i,end=" ")