def happiness(array, set_a, set_b):
    mood = 0
    set_a = set(set_a)
    set_b = set(set_b)

    for num in array:
        if num in set_a:
            mood += 1
        elif num in set_b:
            mood -= 1
    print(mood)