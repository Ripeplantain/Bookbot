import sys

path_to_book = "./books/frankenstein.txt"

def count_words(file: str) -> int:
    words = file.split()

    if words == "":
        return 0
    return len(words)

def count_letters(file: str):
    lowered_string = file.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_dictionary = {letter: 0 for letter in alphabet}
    for letter in lowered_string:
        if letter in alphabet:
            letter_dictionary[letter] += 1
    return letter_dictionary

def main():
    with open(path_to_book) as book: 
        book_contents = book.read()
        print(f"--- Begin report of {path_to_book}---")
        print(f"{count_words(book_contents)} words was found in the document")
        print("\n")
        for key, value in count_letters(book_contents).items():
            print(f"The {key} was found {value} times")
        print("---End Report---")

if __name__ == '__main__':
    sys.exit(main())