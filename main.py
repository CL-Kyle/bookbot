from stats import get_book_num
from stats import get_book_char
from stats import sort_on
from stats import dict_list
from stats import alpha_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    num_words = get_book_num(get_book_text("books/frankenstein.txt"))
    # print(f"{num_words} words found in the document")
    dict_var = get_book_char(get_book_text("books/frankenstein.txt"))
    # print(dict_var)
    char_dict_list = dict_list(dict_var)
    char_dict_list.sort(reverse=True, key=sort_on)
    # print(char_dict_list)
    # print(alpha_list(char_dict_list))
    alpha_list_prime = alpha_list(char_dict_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in alpha_list_prime:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    
main()