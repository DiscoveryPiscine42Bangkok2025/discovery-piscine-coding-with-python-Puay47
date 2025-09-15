import sys

def shrink(s):
    print(s[:8])  # แสดง 8 ตัวแรก

def enlarge(s):
    while len(s) < 8:
        s += "Z"  # เติม Z ไปเรื่อย ๆ
    print(s)

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:  # เท่ากับ 8 ตัวพอดี
            print(arg)
