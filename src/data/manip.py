# Open the file in read mode and read all lines
with open('src/data/students.txt', 'r') as file:
    lines = file.readlines()

# Open the file in write mode to overwrite it
with open('src/data/students.txt', 'w') as file:
    # Iterate through each line
    for line in lines:
        # Strip trailing newline character and append ', 7'
        modified_line = line.rstrip('\n') + ', 7\n'
        # Write the modified line back to the file
        file.write(modified_line)
        print(modified_line)


# Open a file in write mode (creates a new file if it doesn't exist)
with open('example.txt', 'w') as file:
    # Write some content to the file
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This ine 3.\n")
