def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count_map = {}

    for char in text:
        char = char.lower()
        if char not in char_count_map:
            char_count_map[char] = 1
        else:
            char_count_map[char] += 1
    
    return char_count_map