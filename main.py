def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()

from stats import count_words

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    num_words = count_words(file_contents)
    print(f"{num_words} words found in the document")

main()
