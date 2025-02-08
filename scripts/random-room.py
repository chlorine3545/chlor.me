# 用来随机分配房间号的小东西 (/ω＼)
import random


def generate_room():
    floor = str(random.randint(1, 14)).zfill(2)  # 01-14
    room = str(random.randint(1, 99)).zfill(2)  # 01-99
    wing = random.choice(["A", "B"])  # A or B
    return f"{floor}{room}{wing}"


print(generate_room())
