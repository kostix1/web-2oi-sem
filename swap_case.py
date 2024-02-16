def swap_case(str):
    result = ""
    for i in str:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    return result