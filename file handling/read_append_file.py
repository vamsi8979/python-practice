def read_file(filename):
    # Open the file in read mode
    file = open(filename, "r")

    # Read the contents of the file
    content = file.read()

    # Close the file
    file.close()

    # Print the contents
    print(content)

def append_file(filename,content):
    # Open the file in append mode
    file = open(filename, "a")

    # Append content to the file
    file.write(content)

    # Close the file
    file.close()

read_file("example.txt")
print()
print("After Appending into the file")
append_file('example.txt','\nThis is additional text.')
print()
read_file("example.txt")

