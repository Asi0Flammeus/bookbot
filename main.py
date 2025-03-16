from stats import get_num_words, count_character, sort_dictionnary
def get_boot_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def print_report(filepath, num_words, sorted_dictionnary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_dict in sorted_dictionnary:
        if character_dict["character"].isalpha():
            print(f"{character_dict['character']}: {character_dict['num']}")
    print("============= END ==============")

def main():
    filepath = "./books/frankenstein.txt"
    content = get_boot_text(filepath)
    num_words = get_num_words(content)
    character_count = count_character(content)
    sorted_dictionnary = sort_dictionnary(character_count)
    print_report(filepath, num_words, sorted_dictionnary)



main()
