def main():
    text = get_book_text('/home/onno/workspace/github.com/onno1234/bookbot/bookbot/books/frankenstein.txt')
    num_words = count_words(text)
    print(f'{num_words} words found in the document')

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def count_words(text):
    counter = 0
    text_list = text.split()
    for word in text_list:
        counter += 1
    return counter

main()
