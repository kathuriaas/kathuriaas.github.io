# Read, write, modify files using python

Paste following code into a file called `files.py` and run `python files.py`

This will create a file with name specified, write/read/append sample data into the file.

```python
def write_file(file_nm):
    # Open file in write mode
    file_object = open(file_nm, "w")

    # Write file
    file_object.write("Line-1\n")
    file_object.write("Line 2\n")
    file_object.write("Line 3\n")
    file_object.write("Line-4\n")

    # Close file
    file_object.close()


def read_file(file_nm):
    # Open file in read mode
    file_object = open(file_nm, "r")

    # Write file
    print(file_object.read())

    # Close file
    file_object.close()


def read_file_part(file_nm, nm_chars):
    # Open file in read mode
    file_object = open(file_nm, "r")

    # Read file part
    print(file_object.read(nm_chars))

    # Close file
    file_object.close()


def append_file(file_nm):
    # Open file in append mode
    file_object = open(file_nm, "a")

    # Append file
    file_object.write("Appended Line 5\n")
    file_object.write("Appended Line 6\n")
    file_object.write("Appended Line 7\n")
    file_object.write("Appended Line 8\n")

    # Close file
    file_object.close()


def read_line_by_line_file(file_nm):
    # Open file in read mode
    file_object = open(file_nm, "r")

    # Read file with readline method
    # print Line#1
    print(file_object.readline())
    # print Line#2
    print(file_object.readline())

    # Close file
    file_object.close()


def read_file_using_with(file_nm):
    # Open file in read mode using with clause to automatically close the file
    with open(file_nm, "r") as file_object:
        file_data = file_object.readlines()
    print(file_data)


def main():
    # Prompt for file name
    print('Enter file name with complete path:')
    x = input()
    write_file(x)
    read_file(x)
    print("Read first 10 char of file")
    read_file_part(x, 10)
    append_file(x)
    print("File after appending")
    print(read_file(x))
    read_line_by_line_file(x)
    read_file_using_with(x)


if __name__ == "__main__":
    # calling the main function
    main()
```
