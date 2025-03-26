def word_count(path_to_file):
    num_words = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return (f"{num_words} words found in the document")
