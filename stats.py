def get_word_count(string_to_count):
    word_count = 0
    word_count = len(string_to_count.split())
    return str(word_count)

def get_character_count(book_text):
    return_dict = {}
    list_of_characters = list(book_text)
    for character in list_of_characters:
        is_character_present = character.lower() in return_dict
        if is_character_present:
            #Already Exists, Iterate
            return_dict[character.lower()] += 1
        else:
            #New Character, Initialize
            return_dict[character.lower()] = 1
    return return_dict

def book_count(dict):
    return dict["count"]

def pretty_print_character_count(book_text):
    book_dict = get_character_count(book_text)
    book_list =[]
    for character, count in book_dict.items():
        if not character.isalpha():
            continue
        book = {}
        book["character"] = character
        book["count"] = count
        book_list.append(book)
    book_list.sort(reverse=True, key=book_count)
    for book in book_list:
        print(f"{book["character"]}: {book["count"]}")