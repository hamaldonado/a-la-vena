
def is_leap_year(year):
    if a % 100 == 0:
        if a % 400 == 0:
            return True
        else:
            return False

    elif a % 4 == 0:
        return True

    else:
        return False


if __name__ == "__main__":

    a = int(input("Dame un año:"))

    if is_leap_year(a):
        print ("El año ingresado SI es bisiesto")
    else:
        print ("El año ingresado NO es bisiesto")