# define the main function
def main ():
    # open and read file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  # Read the file contents

    # print the contents of the file to the console
    print(file_contents)

# call the maain function to execute the program
if __name__=="__main__":
    main()