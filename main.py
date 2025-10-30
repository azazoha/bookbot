from stats import get_num_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def main():
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print(count_characters(book))
    
main()