def get_num_words(content):
    return len(content.split())


def count_character(content):
    words = content.split()
    character_count = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    return character_count
