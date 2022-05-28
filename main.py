# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    txtFile = open(filename, "r")
    return txtFile.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    wordCount = dict()
    words = text.split()
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount
print(count_words())