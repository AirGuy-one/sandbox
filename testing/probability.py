from random import randint

results = [0] * 4
for i in range(100):
    value = randint(1, 4)
    if value == 1:
        results[0] += 1
    elif value == 2:
        results[1] += 1
    elif value == 3:
        results[2] += 1
    elif value == 4:
        results[3] += 1

print(results)
