from collections import defaultdict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Handle invalid (empty) text
    if is_invalid_text(text):
        return
    
    num_words = get_num_words(text)
    char_count_dict = count_all_characters(text)
    print_report(book_path, num_words, char_count_dict)


def get_book_text(path):
    try:
        # Attempt to open and read the file
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        # Handle the file not being found
        print(f"Error: The file at '{path}' was not found.")
        return ""
    except PermissionError:
        # Handle the case where we lack permission to read the file
        print(f"Error: Permission denied for accessing the file at '{path}'.")
        return ""
    
def is_invalid_text(text):
    is_empty = len(text.strip()) == 0  # Handle text with only whitespace
    if is_empty:
        print("Error: The file is empty or could not be processed.")
    return is_empty

def get_num_words(text):
    words = text.split()
    return len(words)


def count_all_characters(text):
    """
    Counts all characters in the input text (case insensitive).
    Returns a dictionary where the keys are characters and values are occurrence counts.
    """
    characters = defaultdict(int)
    lowercase_text = text.lower()
    for char in lowercase_text:
        characters[char] += 1
    return characters


def sort_dict(unsorted_dict):
    return sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True)

def print_report(book_path, word_count, char_count_dict):
    """
    Prints an analysis report of the text file, including the word count
    and frequency of alphabetic characters sorted by occurrence.
    """
    sorted_dict = sort_dict(char_count_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for entry, count in sorted_dict:
        if entry.isalpha():
            print(f"the '{entry}' character was found {count} times")
    print("--- End report ---")

main()