import re

print("---Liner Search---")
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []
with open("dictionary.txt", "r") as file:
    for line in file:
        dictionary_list.append(line.strip().upper())

with open ("AliceInWonderLand200.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            if word.upper() not in dictionary_list:
                print(f"Line {line_number} possible misspelled word {word}")

