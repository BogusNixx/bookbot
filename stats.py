def word_count(text):
        num_words = len(text.split())
        print(f"{num_words} words found in the document")

def char_count(text):
        dictionary = {}
        for char in text.lower():
                dictionary[char] = dictionary.get(char, 0) + 1
        return dictionary

def sorted_char_count(character_count):
        highest_so_far = float("inf")
        sorted_list = []
        for key, value in character_count:
                if value < highest_so_far:
                        sorted_list.append(key, value)
        print(sorted_list)