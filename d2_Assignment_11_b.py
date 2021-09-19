n1=int(input("Enter the lower range(greater than 0): "))
n2=int(input("Enter the upper range: "))
i=n1
if n1>0:
    print("Perfect numbers are:",end=" ")
    while i<n2:
        j,s=1,0
        while j<i:
            if(i%j==0):
                s=s+j
            j=j+1
        if(s==i):
            print(i,end=" ")
        i=i+1