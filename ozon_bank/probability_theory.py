from random import randint

results = [0] * 4

for i in range(100):
    number = randint(1, 100)

    if 1 <= number <= 25:
        results[0] += 1
    elif 26 <= number <= 50:
        results[1] += 1
    elif 51 <= number <= 75:
        results[2] += 1
    else:
        results[3] += 1

print(results)
print(min(results))
