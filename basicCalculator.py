print("Select an operation: ")
print("1. Add")
print("2. Substract")
print("4. Multiply")
print("5. Divide")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is: " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is: " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is: " + str(int(num1) * int(num2)))

elif operation == "4": 
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is: " + str(int(num1) / int(num2)))

else:
    print("Invalid Entry")