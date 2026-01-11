def wordcount(content):
    words = content.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return (f"Found {wordcount} total words")

def character_count(content):
    characters = list(content)
    letters = {}
    for character in characters:
        if character.lower() not in letters:
            letters[character.lower()] = 1
        else:
            letters[character.lower()] += 1

    return letters