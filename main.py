from stats import get_num_words, count_character
def get_boot_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    filepath = "./books/frankenstein.txt"
    content = get_boot_text(filepath)
    num_words = get_num_words(content)
    character_count = count_character(content)
    print(f"{num_words} words found in the document")
    print(character_count)

main()
