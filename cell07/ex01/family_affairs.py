def find_the_redheads(family):
    # ใช้ filter เพื่อเลือกเฉพาะ key ที่ value เป็น "red"
    redheads = filter(lambda name: family[name] == "red", family.keys())
    return list(redheads)


# ทดสอบการทำงาน
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
