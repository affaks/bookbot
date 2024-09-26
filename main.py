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

def print_report(word_count, char_count):
    # Start of the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Convert character count dictionary to a list of tuples and sort it
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # Print character counts
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    # End of the report
    print("--- End report ---")

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

     # Print the report
    print_report(word_count, char_count)  # Call the report function

# call the main function to execute the program
if __name__=="__main__":
    main()