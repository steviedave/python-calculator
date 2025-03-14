print("PYTHON CALCULATOR")
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operation = input("Enter operation(+, -, *, /): ")

if operation == '+':
  answer = num_1 + num_2
  print (f"{num_1} + {num_2} = {answer}")

elif operation == '-':
  answer = num_1 - num_2
  print (f"{num_1} - {num_2} = {answer}")

elif operation == '*':
  answer = num_1 * num_2
  print (f"{num_1} x {num_2} = {answer}")

elif operation == '/':
  answer = num_1 / num_2
  print (f"{num_1} / {num_2} = {answer}")

else:
  print("Invalid operation! Please try again.")

