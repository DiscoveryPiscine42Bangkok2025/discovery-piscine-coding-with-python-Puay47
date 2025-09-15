def what_is_your_name():
    first_name = input("Hey, what's your first name? : ").strip()
    last_name  = input("And your last name? : ").strip()
    return f"{first_name} {last_name}"

print(f"Well, pleased to meet you, {what_is_your_name()}.")