import itertools


def brute_force_attack(target_password):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    print(type(itertools.product(chars, repeat=4)))
    first = next(itertools.product(chars, repeat=4))
    first_ = list(first)
    print(first_)
    print(''.join(first_))
    attempt = 0
    for password in itertools.product(chars, repeat=4):
        guess = ''.join(password)
        attempt += 1
        if guess == target_password:
            print(f"Password found: {guess}")
            print(f'Attempts number is {attempt}')
            return guess
    return None


target_password = "a1b2"
brute_force_attack(target_password)
print(36 ** 4)
