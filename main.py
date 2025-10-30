def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    

def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def main():
    book = "books/frankenstein.txt"
    num_words = get_num_words(get_book_text(book))
    print(f"Found {num_words} total words")
    
main()