from stats import get_book_num
from stats import get_book_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    num_words = get_book_num(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    dict_var = get_book_char(get_book_text("books/frankenstein.txt"))
    print(dict_var)
main()