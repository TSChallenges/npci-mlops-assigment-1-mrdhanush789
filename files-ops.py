import os
import sys

# Function to create a directory
def create_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Function to change the current working directory
def change_directory(dir_name):
    try:
        os.chdir(dir_name)
        print(f"Changed current directory to '{dir_name}'.")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.")
    except Exception as e:
        print(f"Error changing directory: {e}")

# Function to delete a directory
def delete_directory(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.")
    except OSError:
        print(f"Directory '{dir_name}' is not empty or cannot be removed.")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# Function to list files in the current directory
def list_dir():
    try:
        files = os.listdir()
        if files:
            print("Files in the current directory:")
            for file in files:
                print(file)
        else:
            print("The directory is empty.")
    except Exception as e:
        print(f"Error listing directory contents: {e}")

# Function to display the current working directory
def display_pwd():
    try:
        current_dir = os.getcwd()
        print(f"Current directory: {current_dir}")
    except Exception as e:
        print(f"Error displaying the current directory: {e}")

# Function to create a file
def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            pass
        print(f"File '{file_name}' is created.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Function to write to a file
def write_file(file_name):
    try:
        contents = input("Enter the contents to write into the file: ")
        with open(file_name, 'w') as f:
            f.write(contents)
        print(f"Contents written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to read from a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            contents = f.read()
        print(f"Contents of '{file_name}':\n{contents}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Function to delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Main menu for user interaction
def main():
    while True:
        print("\nMenu:")
        print("1. Create a directory")
        print("2. Change current directory")
        print("3. Delete a directory")
        print("4. List files in the current directory")
        print("5. Display current working directory")
        print("6. Create a file")
        print("7. Write to a file")
        print("8. Read a file")
        print("9. Delete a file")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            dir_name = input("Enter the directory name: ")
            create_directory(dir_name)
        elif choice == '2':
            dir_name = input("Enter the directory name: ")
            change_directory(dir_name)
        elif choice == '3':
            dir_name = input("Enter the directory name: ")
            delete_directory(dir_name)
        elif choice == '4':
            list_dir()
        elif choice == '5':
            display_pwd()
        elif choice == '6':
            file_name = input("Enter the file name: ")
            create_file(file_name)
        elif choice == '7':
            file_name = input("Enter the file name: ")
            write_file(file_name)
        elif choice == '8':
            file_name = input("Enter the file name: ")
            read_file(file_name)
        elif choice == '9':
            file_name = input("Enter the file name: ")
            delete_file(file_name)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()