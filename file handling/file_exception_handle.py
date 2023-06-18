def read_file(filename):
    file = None  # Initialize the file variable

    try:
        # Open the file in read mode
        file = open(filename, "r")

        # Read the file line by line
        for line in file:
            # Process each line
            print(line)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    except IOError:
        print("Error reading the file.")

    finally:
        if file:
            print(f"\nFile: '{filename}' is closed\n")
            file.close()  # Close the file if it is defined

filename = 'example.txt'
print(f"File 1: {filename}")
read_file(filename)
filename = 'test.txt'
print(f"File 2: {filename}")
read_file(filename)

