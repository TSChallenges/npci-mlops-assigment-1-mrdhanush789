import re

# Function to implement 'grep' functionality
def grep(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Search each line for the pattern and print matching lines
            for line in lines:
                if re.search(pattern, line):
                    print(line.strip())  # .strip() to remove any extra newlines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Function to implement 'sed' functionality
def sed(old_pattern, new_pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Replace occurrences of old pattern with the new pattern in each line
        with open(file_name, 'w') as file:
            for line in lines:
                new_line = line.replace(old_pattern, new_pattern)
                file.write(new_line)
        print(f"Replaced '{old_pattern}' with '{new_pattern}' in file '{file_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

# Function to implement 'awk' functionality
def awk(n, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            # Extract and print the nth column from each line
            for line in lines:
                columns = line.split()
                if len(columns) >= n:
                    print(columns[n - 1])  # n-1 to adjust for 0-based indexing
                else:
                    print(f"Line does not have {n} columns.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

# Main function to handle user input and call the appropriate function
def main():
    file_name = input("Enter the file name: ")
    command = input("Enter the command (grep, sed, awk): ").strip().lower()

    if command == 'grep':
        pattern = input("Enter the pattern to search for: ")
        grep(pattern, file_name)
    elif command == 'sed':
        old_pattern = input("Enter the old pattern to replace: ")
        new_pattern = input("Enter the new pattern: ")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number: ")
        try:
            num = int(n)
            if num > 0:
                awk(num, file_name)
            else:
                print("Please enter a positive integer for the column number.")
        except ValueError:
            print("Invalid input. Column number must be an integer.")
    else:
        print("Command is invalid. Please enter 'grep', 'sed', or 'awk'.")

if __name__ == "__main__":
    main()