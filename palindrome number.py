n = int(input("enetr the number "))
rev = 0
temp = n
while n!=0:
    num = n%10
    rev = rev*10+num
    n = n//10
if(temp == rev):
    print("number is palindrome ")
else:
    print("number is not pallindrome ")