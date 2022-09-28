def search4vowels(phrase:str) -> set:
    """Возвращает гласные, найденные в указанной фразе"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:set, letters:str='aeiou') -> set:
    """Возращает множество букв из множества 'letters',
       найденных в указанной фразе 'phrase'"""
    return set(letters).intersection(set(phrase))




    
print(search4vowels("Hello"))
