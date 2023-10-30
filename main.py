year = 2024

def isLeapYear(year):
    if year%4 == 0 and year%100!=0:
        return True
    elif year%100==0:
        return True
    return False

print(isLeapYear(year))