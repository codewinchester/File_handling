# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 789\n")
    except Exception as e:
        print("Error occurred while creating the file:", e)

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied while reading the file.")
    except Exception as e:
        print("Error occurred while reading the file:", e)

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("67890\n")
            file.write("Another line added through append mode\n")
    except Exception as e:
        print("Error occurred while appending to the file:", e)

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()
