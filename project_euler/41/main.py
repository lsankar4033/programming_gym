import itertools


def is_prime(number: int) -> bool:
    for divisor in itertools.count(2):
        if number % divisor == 0:
            return False
        if divisor * divisor > number:
            return True

def solution_permutations() -> int:
    for digits in reversed(list(itertools.permutations("1234567"))):
        number = int("".join(digits))
        if is_prime(number):
            return number

print(solution_permutations())
