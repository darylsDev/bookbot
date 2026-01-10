def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def wordcount():
    content = get_book_text(filepath)
    words = content.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return (f"Found {wordcount} total words")

def main():
    content = get_book_text(filepath)
    count = wordcount()
    print(content)
    print(count) 

filepath = "./books/frankenstein.txt"
main()
