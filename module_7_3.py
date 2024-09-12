import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(p, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        for name, words in self.get_all_words().items():
            if word in words:
                word_positions[name] = words.index(word) + 1
            else:
                word_positions[name] = -1
        return word_positions

    def count(self, word):
        word = word.lower()
        word_count = {}
        for name, words in self.get_all_words().items():
            word_count[name] = words.count(word)
        return word_count

finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # Позиция первого слова 'text'
print(finder2.count('teXT'))     # Количество слова 'text'