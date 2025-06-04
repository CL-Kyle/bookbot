def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def get_book_num(contents):
    list_contents = contents.split()
    list_count = len(list_contents)
    return list_count


def main():
    num_words = get_book_num(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
main()