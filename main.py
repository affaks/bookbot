#count words
def count_words(text):
    words = text.split() # Split the text into words
    return len(words) # return the number of words

def main ():
    # open and read file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  # Read the file contents

    # Count the words and print the result
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

# call the main function to execute the program
if __name__=="__main__":
    main()