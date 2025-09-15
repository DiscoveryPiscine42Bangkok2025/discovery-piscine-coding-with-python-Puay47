# multiplication_table.py

s = input("Enter a number\n").strip()

try:
    n = int(s)
    for i in range(10):           # 0..9
        print(f"{i} x {n} = {i * n}")
except ValueError:
    # ถ้าพิมพ์ไม่ใช่ตัวเลข แสดง Error (เผื่อกรณีอินพุตไม่ถูกต้อง)
    print("Error")
