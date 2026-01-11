from stats import wordcount, character_count, character_list, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
              
def main():
    content = get_book_text(filepath)
    count = wordcount(content)
    c_dict = character_count(content)
    c_list = character_list(c_dict)
    
    c_list.sort(reverse=True,key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count)
    print("--------- Character Count -------")
    for c in c_list:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    

filepath = "./books/frankenstein.txt"
main()
