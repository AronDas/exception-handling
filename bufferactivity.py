def check_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        elif age % 2==0:
            print("The age is even")
        else:
            print("The age is odd")
        
    except ValueError as e:
        print("Invalid age entered:", e)

user_input = int(input("Please enter your age here:"))
check_age(user_input)