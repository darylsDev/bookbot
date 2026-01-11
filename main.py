from stats import wordcount, character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
              
def main():
    content = get_book_text(filepath)
    count = wordcount(content)
    character = character_count(content)
    print(content)
    print(count)
    print(character)

filepath = "./books/frankenstein.txt"
main()
