year=int(input("enter your year:"))
if year%400==0:
  print("%d given year is leap year"%year)
elif year%100==0:
  print("%d is not a leap year" %year)
elif year%4==0:
  print("%d is a leap year" %year)
else:
  print("%d is not leap year" %year)