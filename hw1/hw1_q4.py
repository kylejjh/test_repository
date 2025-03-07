'''
4.Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
'''

def count_vowels(word):
    vowels = "aeiouAEIOU"  # Define vowels
    count = 0  # Initialize counter

    for char in word:
        if char in vowels:
            count += 1

    return count

word = "apple"
print(f"There are {count_vowels(word)} vowels in this word.")