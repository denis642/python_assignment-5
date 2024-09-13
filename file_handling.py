

# File Creation and Writing
try:
    # Creating and writing to the file
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line with a number: 42.\n")
        file.write("Final line in the initial file.\n")
    print("File created and initial content written successfully.")
except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# File Reading and Display
try:
    # Reading and displaying the file content
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("\nFile content after initial writing:")
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# File Appending
try:
    # Opening the file in append mode and adding more content
    with open("my_file.txt", 'a') as file:
        file.write("Appending first additional line.\n")
        file.write("Appending second line with a number: 100.\n")
        file.write("This is the final appended line.\n")
    print("\nContent appended successfully.")
except FileNotFoundError:
    print("Error: File not found for appending.")
except Exception as e:
    print(f"An unexpected error occurred while appending to the file: {e}")

# Reading the file again to show appended content
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("\nFile content after appending:")
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

finally:
    print("\nEnd of file operations.")
