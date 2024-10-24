def is_prime(func):
    def wrapper(*args, **kwargs):
        base_result = func(*args, **kwargs)
        if base_result < 2:
            return f"Составное\n{base_result}"
        for i in range(2, int(base_result**0.5) + 1):
            if base_result % i == 0:
                return f"Составное\n{base_result}"

        return f"Простое\n{base_result}"
    return wrapper

@is_prime
def sum_three(*nums):
    _sum = sum(nums)
    return _sum

result = sum_three(2, 3, 6)
print(result)