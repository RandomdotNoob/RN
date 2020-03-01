# Check if the first number is a number
# If not raise an exception () and continue in the loop until a number is given
# If a number is given it, the program will reach line 10 and go on with execution
while True:
    try:
        num1 = int(input("Enter a Number: "))
    except ValueError:
        print('You have to insert a number')
        continue
    break

#do sth similar for the second one too

num2 = input("Enter a second Number: ")
operator = input("Enter an operator: ")

if operator == '+':
    result = float(num1) + float(num2)
    print(result)
elif operator == '-':
    result = float(num1) - float(num2)
    print(result)
elif operator == '*':
    result = float(num1) * float(num2)
    print(result)
elif operator == '/':
    result = float(num1) / float(num2)
    print(result)
else:
    input("Please enter a valid operator: ")
