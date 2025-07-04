
# Takes text of book returns number of words
def get_book_num(contents):
    list_contents = contents.split()
    list_count = len(list_contents)
    return list_count

# Takes text of book returns a dictionary of total number of each character
def get_book_char(contents):
    contents_lower = contents.lower()
    char_dict = {}
    for char in contents_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# Takes dictionary of total characters returns a list of dictionaries with key/value pair of "char" and "num"
def dict_list(char_dict):
    char_dict_list = []
    for char in char_dict:
        num = char_dict[char]
        small_dict = {"char": char, "num": num}
        char_dict_list.append(small_dict)
    return char_dict_list

def sort_on(dict):
    return dict["num"]

# Takes list of dictionaries returns a list of characters only in the English language
def alpha_list(char_dict_list):
    alpha_list =[]
    for char in char_dict_list:
        if char["char"].isalpha() and char["char"] in "abcdefghijklmnopqrstuvwxyz":
            alpha_list.append(char)
    return alpha_list
