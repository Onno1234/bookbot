def count_words(text):
    counter = 0
    text_list = text.split()
    for word in text_list:
        counter += 1
    return counter

def count_letters(text):
    unique_char_list = []
    char_list = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in unique_char_list:
            unique_char_list.append(lower_char)
            char_list[lower_char] = 1
        else:
            char_list[lower_char] += 1
    return char_list

def sort_on(items):
    return items["amount"]

def sort_dictionary(dictionairy):
    list_of_dicts = []
    for char in dictionairy:
        value = dictionairy[char]
        tiny_dict = {'letter':char,'amount':value}
        list_of_dicts.append(tiny_dict)
    list_of_dicts.sort(reverse=True,key=sort_on)
    return list_of_dicts