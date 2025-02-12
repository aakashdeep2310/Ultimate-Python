import os

# Get the current directory
directory = os.path.dirname(os.path.realpath(__file__))

# Get the contents of the directory
contents = os.listdir(directory)

# Print the contents of the directory
for item in contents:
    print(item)