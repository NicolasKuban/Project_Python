def cache_args(func):
    # полезный код
    relust_calculate = {}
    def save_calculate(value, *args):
        if value not in relust_calculate:
            relust_calculate[value] = func(value)
        else:
            print(f"==== Быстро и легко {value} ====")
        return relust_calculate[value]
    return save_calculate

@cache_args
def long_heavy(num):
     print(f"==== Долго и сложно {num} ====")
     return num**num

print(long_heavy(1))

# Долго и сложно 1
print(long_heavy(1))
print(long_heavy(2))

# Долго и сложно 2
# 4
print(long_heavy(2))
# 4
print(long_heavy(3))
# Долго и сложно 1
print(long_heavy(4))
print(long_heavy(1))

# Долго и сложно 2
# 4
print(long_heavy(4))
# 4
print(long_heavy(9))
