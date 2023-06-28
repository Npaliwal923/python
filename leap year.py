year = int(input("enetr the year" ))

if year%400==0:
    print("year is leap year ")
else:
    if year%4==0 and year%100 != 0:
        print("number is leap year ")
    else:
        print("number is not the leap year ")
