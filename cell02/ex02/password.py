password = "OpenSesame"

input_password = input("Enter the password: ").strip()

if input_password == password:
    print("ACCESS GRANTED.")
else:
    print("ACCESS DENIED.")