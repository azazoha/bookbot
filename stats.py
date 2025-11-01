def get_num_words(book):
    num_words = book.split()
    return len(num_words)

def count_characters(book):
    t = book.lower()
    char_count = {}
    for char in t:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_char_count(book_characters):
    char_count_pair = []
    sorted_char_count = []
    for char in book_characters:
        char_count_pair.append({"char": char, "num": book_characters[char]})
    sorted_char_count = sorted(char_count_pair, key=lambda x: -x["num"])
    return sorted_char_count