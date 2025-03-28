from stats import get_word_count
from stats import pretty_print_character_count
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print(f"Found " + get_word_count(book_text) + " total words")
    print("--------- Character Count -------")
    pretty_print_character_count(book_text)
    print("============= END ===============")
main()