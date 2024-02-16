def anagram(str1, str2):
    if len(str1) != len(str2):
        print("No")
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("Yes")