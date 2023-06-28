n = int(input("enetr the number "))
arm = n
sum = 0
while n!=0:
    num = n%10
    sum = sum + num**3
    n = n//10
if(arm == sum):
    print("number is armstrong ",arm)
else:
    print("number is not armstrong ")
    