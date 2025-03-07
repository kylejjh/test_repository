'''
3.string = """

I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!

"""

#Your task is to count the number of different words in this text
'''


def count_unique_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        text = text.lower()  # convert to lowercase

        # Remove punctuation and clean words
        words = []
        for word in text.split():  # Split the text into words
            filtered_chars = []  # Set an empty list to store filtered characters
            for char in word:  # Loop through each character in the word
                if char.isalnum():  # Check if the character is letters or numbers
                    filtered_chars.append(char)

            cleaned_word = ''.join(filtered_chars)  # get the world from the lst to str

            if cleaned_word:  # Avoid empty word
                words.append(cleaned_word)

        unique_words = set(words)  # Store unique words in a set
        return len(unique_words)


    except FileNotFoundError:
        print("Error: File not found!")
        return None


filename = "hw1_q3_text.txt"  # Replace with the actual filename
print("Number of different words:", count_unique_words_from_file(filename))