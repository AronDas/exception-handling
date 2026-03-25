try:
    number = int(input("please enter a number:"))
    print("The number entered is", number)
except ValueError as ex:
    print("exception", ex)