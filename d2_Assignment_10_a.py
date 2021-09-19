n=int(input("Enter the upper limit: "))
a,b=0,1
sum= 0
print("Fibonacci Series unto",n,"is: ")
while(sum <= n):
  print(sum, end = " ")
  a = b
  b = sum
  sum = a + b