def cache_args(func):
    last_args = {}
    def save_args(num, *args):
        if num not in last_args:
            last_args[num] = func(num)
        return last_args[num]
    return save_args


@cache_args
def long_heavy(num):
    print(f"Долго и сложно {num}")
    return num**num

print(long_heavy(1))
# Долго и сложно 1
# 1

print(long_heavy(1))
# 1

print(long_heavy(2))
# Долго и сложно 2
# 4

print(long_heavy(2))
# 4

print(long_heavy(2))
# 4
print(long_heavy(3))
# 4
print(long_heavy(1))
# 4
print(long_heavy(2))
# 4
print(long_heavy(4))
# 4
