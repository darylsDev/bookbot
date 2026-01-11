#provides a word count using the original content
def wordcount(content):
    words = content.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return (f"Found {wordcount} total words")

#provides a count for each letter in the form of a dictionary {a: 123, b:234, c:345}
def character_count(content):
    characters = list(content)
    letters = {}
    for character in characters:
        if character.lower() not in letters:
            letters[character.lower()] = 1
        else:
            letters[character.lower()] += 1
    return letters

#breaks down the dictionary into 2 key-value pairs as "char" and "num", which are inserted into a list [{'char': a, 'num': 123}, {'char': b, 'num': 234}, {'char': 3, 'num': 345}]
def character_list(c_dict):
    character_list = [] #create empty list
    for character in c_dict:
        if character.isalpha(): 
            character_dict = {} 
            character_dict["char"] = character 
            character_dict["num"] = c_dict[character] 
            character_list.append(character_dict) 
    return character_list

#return list of 'num' key value pairs
def sort_on(c_list):
    return c_list["num"]