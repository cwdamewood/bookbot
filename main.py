import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    
def get_book_text(filepath):
    with open(filepath) as book_file:
        book_text = book_file.read()
    return(book_text)

from stats import count_words
from stats import count_characters
from stats import sorted_char



book_text = get_book_text(filepath)
num_words = count_words(book_text)
char_count = count_characters(book_text)
sorted_chars = sorted_char(char_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["num"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")
