from random import randint

a = tuple(randint(1, 10) for i in randint(1, 101))

a = tuple(i for i in range(1, 101))

print(a)