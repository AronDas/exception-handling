valid = False
while not valid:
    try:
        n = int(input("Please enter a number here:"))
        while n%2==0:
            print("bye")

        valid = True
    except ValueError:
        print("Invalid input")