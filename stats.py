def sort_list(dict):
    return dict[char]

def count_letters(book):
    book_text = book.lower()
    character_count = {}
    for char in book_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def num_words(book):
    words = book.split()
    return len(words)
