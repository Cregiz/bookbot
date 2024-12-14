def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = count_words(text)
    char_count = count_chars(text)

    print_report(book_path, word_count, char_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
    return char_count

def print_report(path, word_count, char_count):
    print(f"--- Begin report of {path}")
    print(f"{word_count} words found in the document\n")

    sorted_char_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")

    print ("--- End report ---")    
main()