import sys
from stats import word_count, char_count, sorted_char_count

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    words_counted = word_count(text)
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    chars = char_count(text)
    sorted_chars = sorted_char_count(chars)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()