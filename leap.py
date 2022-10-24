def yr():
    n=int(input("enter a year"))
    if n%4==0 and not(n%100==0) or n%400==0:
        print("leap year")
    else:
        print("not leap year")

yr()
