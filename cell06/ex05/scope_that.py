def add_one(n):
    return n + 1

# กรณีที่ 1: ไม่เก็บค่าที่ return
x = 5
print("Before (case 1):", x)
add_one(x)   # เรียกใช้แต่ไม่เก็บค่า
print("After (case 1):", x)  # ค่าไม่เปลี่ยน

print("------")

y = 5
print("Before (case 2):", y)
y = add_one(y)  # เก็บค่าที่ return กลับมา
print("After (case 2):", y)  # ค่าเปลี่ยน
