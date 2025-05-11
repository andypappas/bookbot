def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    chars_list = []
    for char, count in dict.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

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
