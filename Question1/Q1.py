#defining the function for leap 
def checkLeapYear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
year = int(input("Please enter a year: "))
print(checkLeapYear(year))
