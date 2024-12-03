import math


def compute_attempts(
    p: float,
    target_p: float,
) -> float:
    return math.log(1 - target_p) / math.log(1 - p)


def main():
    probability = 0.33
    target_probability = 0.99
    attempts_needed = compute_attempts(probability, target_probability)
    print(f"Number of attempts needed: {attempts_needed}")


if __name__ == '__main__':
    main()
