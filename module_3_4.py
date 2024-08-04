def single_root_words(root_words, *other_words):
    same_words = []  # список same_words, который пополнится нужными словами
    root_words_lower = root_words.lower()  # привожу root_words к нижнему регистру
    for word in other_words:  # перебераю предполагаемо подходящие слова
        word_lower = word.lower()  # привожу к нижнему регистру
        # проверяю на содержание текущих слов и наоборот
        if root_words_lower in word_lower or word_lower in root_words_lower:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
