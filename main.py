import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f_obj:
        file_contents = f_obj.read()

    return file_contents

def pretty_print(word_count, char_count_map, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in char_count_map.items():
        print(f"{key}: {value}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    word_count = count_words(content)
    char_count_map = count_characters(content)
    pretty_print(word_count, char_count_map, filepath)
    

if __name__ == "__main__":
    main()