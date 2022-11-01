first_num = float(input("Input first number: "))
second_num = float(input("Input second number: "))
operation = int(input("Choose operation:, either 1. Addition or 2. Subtraction"))
while operation != 1 and operation != 2:
    print("try again! ")
    operation = int(input("Choose operation:, either 1. Addition or 2. Subtraction "))
if operation == 1:
    result = first_num + second_num
elif operation == 2:
    result = first_num - second_num

print(result)
