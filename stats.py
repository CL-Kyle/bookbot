def get_book_num(contents):
    list_contents = contents.split()
    list_count = len(list_contents)
    return list_count

def get_book_char(contents):
    contents_lower = contents.lower()
    char_dict = {}
    for char in contents_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict