# Determine if a year is a leap year. (Leap years are  divisible by 4 but not by 100 unl;ess also divisible by 400)

year = 2024

if(year % 400 ==0) or (year % 4 ==0 and year % 100 !=0 ):
    print( year, "is a leap Year")
else:
    print(year, "is Not a leap Year")
