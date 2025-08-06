# 📂 File Read & Write Challenge + Error Handling Lab

def modify_content(text):
    """
    This function modifies the content of the file.
    For this example, we'll convert all text to uppercase.
    """
    return text.upper()

def main():
    # Ask the user for a filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define the output file name
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"✅ File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
