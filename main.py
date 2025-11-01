import sys
from stats import get_num_words, count_characters, get_sorted_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = get_num_words(book)
    count_chars = count_characters(book)
    sorted_list = get_sorted_char_count(count_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for s in sorted_list:
        if s["char"].isalpha():
            print(f"{s['char']}: {s['num']}")
    print("============= END ===============")
    
main()