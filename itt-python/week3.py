## Problem Statement
Write a Python program to read a text file and perform the following:
1. Count the frequency of repeated words.
2. Calculate the total length of the document (excluding spaces and punctuation).
3. Identify the largest word and display it in reverse.

import os

def count_repeated_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    repeated = {word: count for word, count in word_count.items() if count > 1}
    return repeated

def total_length_no_spaces(text):
   return sum(1 for char in text if char.isalnum())

def find_largest_word_reversed(text):
    words = text.split()
    largest_word = ""
    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word[::-1], largest_word

def read_file(file_name):
    if not os.path.isfile(file_name):
        print("File does not exist.")
        return None
    with open(file_name, "r") as f:
        data = f.read()
    return data

def main():
    file_name = input("Enter the filename to process: ")
    text = read_file(file_name)
    if text is None:
        return

    print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    print(text)
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")

    repeated_words = count_repeated_words(text)
    length = total_length_no_spaces(text)
    largest_word_reversed, largest_word = find_largest_word_reversed(text)

    print(f"Total length of the document (characters): {length}\n")

    if repeated_words:
        print("Repeated words and their counts:")
        for word, count in repeated_words.items():
            print(f"'{word}': {count}")
    else:
        print("No repeated words found.")

    print(f"\nLargest word         : {largest_word}")
    print(f"Largest word reversed: {largest_word_reversed}")
    print("")

main()


```text
Enter the filename to process: sample.txt

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
GitHub is great for coding. Coding is fun.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Total length of the document (characters): 34

Repeated words and their counts:
'is': 2
'coding': 2

Largest word         : coding.
Largest word reversed: .gnidoc
