def word_count(s):
    # list of special characters
    specs = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    # separate words in string
    if len(s) < 1:
        return {}
    counts = {}
    print("s: ",s)
    s = s.lower()
    print("lower-s: ",s)
    newS = s.split(' ')
    print("newS: ", newS)
    # iterate through the string
    for word in newS:
        print("word: ",word)
        # ensure character is a letter
        for character in word:
            print("character: ",character)
            if character.isalpha() or character == "'":
                # if the word is in the dictionary, increment its count 
                continue
            else:
                print(character)
                word = word.replace(character, '')
                print("replaced word: ",word)
        # if the word is in the dictionary, increment its count
        if len(word) >= 1:
            if word in counts:
                counts[word] += 1
            # if not, add it, with value 1
            else:
                counts[word] = 1
    # return the dictionary
    print(counts)
    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))