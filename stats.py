def get_num_words(content):
    return len(content.split())

def count_character(content):
    character_count = {}
    for letter in content:
        letter = letter.lower()
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sort_dictionnary(character_count):
    sorted_character_count = []

    for key in character_count:
        temp_dict = {"character": key, "num": character_count[key]}
        sorted_character_count.append(temp_dict)

    sorted_character_count.sort(reverse=True, key=sort_on)

    return sorted_character_count

