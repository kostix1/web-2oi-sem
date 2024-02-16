import re
def len_of_word():  
    longest_words = []
    max_length = 0

    # Открываем файл и читаем его содержимое
    with open("./example.txt", 'r') as file:
        text = file.read()
    
    # Используем регулярное выражение для извлечения слов из текста
    words = re.findall(r'\b\w+\b', text)

    # Находим максимальную длину слова
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_words = [word]
        elif word_length == max_length:
            longest_words.append(word)

    print(longest_words)