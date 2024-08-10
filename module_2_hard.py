import random


def find_divisible_pair(num):
    pairs = []
    for a in range(1, num):
        for b in range(a + 1, num + 1):
            if num % (a + b) == 0:
                pairs.append((a, b))

    pairs.sort(key=lambda x: (x[0], x[1]))
    return pairs


while True:
    first_number = random.randint(3, 20)
    print(first_number)

    divisible_pairs = find_divisible_pair(first_number)
    if divisible_pairs:
        result = ""
        for pair in divisible_pairs:
            result += f"{pair[0]}{pair[1]}"
        print(result)
        break
    else:
        print('Нет результата')