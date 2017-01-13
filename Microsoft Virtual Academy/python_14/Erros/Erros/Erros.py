import sys

firstNumber = 0.0
secondNumber = 0.0
result = 0

try:
    firstNumber = float(input("enter a number "))
    secondNumber = float(input("enter a number "))
    result = firstNumber / secondNumber
    print(result)
except ZeroDivisionError:
    print("The answe is infinity")
except:
    error = sys.exc_info()[0]
    print("I am sorry something went wrong")
    print(error)
    sys.exit()
finally:
    print("I will always run!!!")