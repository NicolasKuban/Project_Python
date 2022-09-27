def search4vowels(phrase:str) -> set:
    """Возвращает гласные, найденные в указанной фразе"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(search4vowels("Hello"))