def count_words(book_text):
    split_text = book_text.split()
    num_words = len(split_text)
    return(num_words)

def count_characters(book_text):
    chars_dict = {}
    for char in book_text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sorted_char(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        char_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list