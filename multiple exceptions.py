try:
    num1, num2 = eval(input("Please enter two numbers seprated by a comma:"))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Dont divide by zero!")
except SyntaxError:
    print("There is an error, try seperating your numbers with a comma like this 1, 2.")
else:
    print("There are no exceptions")
finally:
    print("This statement will always run")