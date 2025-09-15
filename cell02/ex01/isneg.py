num = input("Enter a number: ").strip()

input_num = int(num)

if input_num < 0:
    print("This number is negative.")
elif input_num > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")