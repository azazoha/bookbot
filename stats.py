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