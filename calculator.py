fnumber = int(input("Insert the first number: "))
snumber = int(input("Insert the second number: "))

operation = input("Insert operation: ")

if operation == "+":
    print(fnumber + snumber)
elif operation == "-":
    print(fnumber - snumber)
elif operation == "*":
    print(fnumber * snumber)
elif operation == "/":
    print(fnumber / snumber)