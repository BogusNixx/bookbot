from stats import word_count, char_count, sorted_char_count

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count(text)
    chars = char_count(text)
    print(chars)
    sorted_char_count(chars)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()
