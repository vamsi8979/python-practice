def read_file(filename):
    # Open the file in read mode
    file = open(filename, "r")

    # Read the contents of the file
    content = file.read()

    # Close the file
    file.close()

    # Print the contents
    print(content)

def write_file(filename, content):
    # Open the file in write mode
    file = open(filename, "w")

    # Write content to the file
    file.write("This is some sample text.")

    # Close the file
    file.close()

read_file("example.txt")
write_file("example.txt","This is some sample text.")
print()
print("After writing into the file")
print()
read_file("example.txt")

