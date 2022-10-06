def uglify(value):
    relust = ""
    for i in range(len(value)):
        if i%2:
            relust += value[i].upper()
        else:
            relust += value[i].lower()
    return relust


s = "Привет Мир!"
print(uglify(s))