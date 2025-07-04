from stats import get_book_num
from stats import get_book_char
from stats import sort_on
from stats import dict_list
from stats import alpha_list
import sys

# Gets text of given book
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        # The meat of the BookBot, all functions working together generating data for the report:
        num_words = get_book_num(get_book_text(sys.argv[1]))
        dict_var = get_book_char(get_book_text(sys.argv[1]))
        char_dict_list = dict_list(dict_var)
        char_dict_list.sort(reverse=True, key=sort_on)
        alpha_list_prime = alpha_list(char_dict_list)

        # Report Format:

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in alpha_list_prime:
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    
main()