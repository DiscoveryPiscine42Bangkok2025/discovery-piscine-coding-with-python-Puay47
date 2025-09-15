def famous_births(scientists):
    # sorted dictionary ตามปีเกิด (date_of_birth)
    sorted_scientists = sorted(scientists.values(), key=lambda x: x["date_of_birth"])

    # แสดงผลเรียงตามปีเกิด
    for person in sorted_scientists:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")


# ตัวอย่างข้อมูลนักวิทยาศาสตร์
women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": 1815},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": 1900},
    "lise": {"name": "Lise Meitner", "date_of_birth": 1878},
    "grace": {"name": "Grace Hopper", "date_of_birth": 1906}
}

famous_births(women_scientists)
