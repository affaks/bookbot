#count words
def count_words(text):
    words = text.split() # Split the text into words
    return len(words) # return the number of words

# count Characters
def count_characters(text):
    char_count = {} 
    for char in text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1 
            else :
                char_count[char] = 1 
    return char_count 

def main ():
    # open and read file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  # Read the file contents

    # Count the words and print the result
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

    # Count the characters and print the result
    char_count = count_characters(file_contents)
    print(char_count)  # Print the character counts

# call the main function to execute the program
if __name__=="__main__":
    main()