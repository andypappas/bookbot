from stats import num_words, count_letters, sort_list

def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    word_count = num_words(book_text)
    letter_count = count_letters(book_text)
    characters = { {"char": 

main()
