from stats import num_words, count_letters, sort_list, sort_on
import sys

def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(args)

    book = args[1]
    book_text = get_book_text(book)
    word_count = num_words(book_text)
    letter_count = count_letters(book_text)
    letters_by_value = sort_list(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    
    for letter_dict in letters_by_value:
        char = letter_dict["char"]
        count = letter_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END =============")


main()
