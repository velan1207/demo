year=int(input("Enter year: "))
print("Welcome to Leap Year Checker")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("Thank you for using the Leap Year Checker!")