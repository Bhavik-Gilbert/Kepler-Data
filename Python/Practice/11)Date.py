n=0
while n==0:
    day = int(input("What is the day number"))
    if day > 0 and day < 32:
        n=1
while n==1:
    month = int(input("What is the month number"))
    if month > 0 and month < 13:
        n=2
while n==2:
    year = int(input("What is the year number"))
    if year <= 2020:
        n=3
print(day,"/",month,"/",year)
