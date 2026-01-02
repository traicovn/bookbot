import sys
def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()

from stats import count_words, char_count, sorted_char_list

def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    
    else:
       path_to_file = (sys.argv[1])
       file_contents = get_book_text(path_to_file)
       num_words = count_words(file_contents)
       print(f"Found {num_words} total words")

       char_counts = char_count(file_contents)
       print("\nCharacter counts:")
       print(char_counts)
    
       counts = char_counts
       sorted_chars = sorted_char_list(counts)
       for entry in sorted_chars:
           print(f"{entry['char']}: {entry['num']}")
       print("--- End report ---")


main()
