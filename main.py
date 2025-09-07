from stats import count_words, count_letters, sort_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    letter_count = count_letters(text)
    sorted_letter_count = sort_dictionary(letter_count)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in range(0,len(sorted_letter_count)):
        small_dict = sorted_letter_count[i]
        char = small_dict['letter']
        chars = small_dict['amount']
        if char not in '•:/&$·[]()#%=/¬~@|¡¿?`+*^,.;:!?></*-+ç0}"“‘:”:™:1234567890-_:\{¨ \º} ’:—' and char != '\n':
            print(f'{char}: {chars}')
    print('============= END ===============')

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents



main()
