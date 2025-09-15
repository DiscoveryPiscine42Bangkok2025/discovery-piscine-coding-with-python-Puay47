num1 = input("Enter the first number: ").strip()
num2 = input("Enter the second number: ").strip()
input_num1 = int(num1)
input_num2 = int(num2)

result = input_num1 * input_num2

print(input_num1, "x", input_num2, "=", result)

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")