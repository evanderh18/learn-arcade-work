import re

print("---Liner Search---")


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dictionary_list = []
# Open Dictionary File
with open("dictionary.txt", "r") as file:
    # Remove double-spacing
    for line in file:
        dictionary_list.append(line.strip().upper())

# Open Alice in Wonderland File
with open("AliceInWonderLand200.txt", "r") as file:
    # Start with line 0
    line_number = 0
    # Add line numbers in text
    for line in file:
        line_number += 1
        word_list = split_line(line)
        # Spell check
        for word in word_list:
            if word.upper() not in dictionary_list:
                print(f"Line {line_number} has a possible misspelled word. Word is: {word}")

