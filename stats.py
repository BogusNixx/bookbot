def word_count(text):
        num_words = len(text.split())
        return num_words

def char_count(text):
        dictionary = {}
        for char in text.lower():
                dictionary[char] = dictionary.get(char, 0) + 1
        return dictionary

def sorted_char_count(character_count):
        sorted_list = []
        for char, count in character_count.items():
                if char.isalpha():
                        char_dict = {"char": char, "count": count}
                        sorted_list.append(char_dict)

        def sort_on(dict):
                return dict["count"]
        
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list