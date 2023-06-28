n = int(input("enetr the number "))
sum = 0
for i in range(1,n):
    if (n%i)==0:
        sum = sum + i
if sum==n :  
   print("number is  perfect")
else:
    print("number is not perfect",n )
