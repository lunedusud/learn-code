import random
name = input("한식, 중식, 일식 중 한가지를 선택해주세요.")
if name == "한식":
    list_a = ["김","이","박"]
    print(random.choice(list_a))
elif name == "중식":
    list_b = ["a","b","c"]
    print(random.choice(list_b))
else:
    list_c = ["아","에","우"]
    print(random.choice(list_c))
