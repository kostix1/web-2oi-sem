def python_if_else(n):
    if n % 2 == 1:
        return "Weird"
    # elif n>= 2 and n<=5 and n % 2 == 0:
    elif n in range(2, 6) and n % 2 == 0:
        return "Not Weird"
    elif n in range(6, 21) and n % 2 == 0:
        return "Weird"
    elif n % 2 == 0 and n >= 20:
        return "Not Weird"

