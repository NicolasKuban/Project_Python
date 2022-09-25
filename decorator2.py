def cache3(func):

    _cache = {"counter": 0, "temp": None}

    def run_func():
        if _cache["counter"] > 2:
            _cache["counter"] = 0
            _cache["temp"] = None
        _cache["counter"] += 1
        if _cache["temp"] is None:
            _cache["temp"] = func()

        return _cache["temp"]

    return run_func

@cache3
def heavy():
    print('Сложные вычисления')
    return 1
##_cache = 1
##print((_cache) is None)
print(heavy())

# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
