import random

random_num = random.randint(1,100)
print(random_num)

if random_num >= 50:
    print('数値は50以上です')
else: print('数値は50未満です')