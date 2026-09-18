def analyze_file():
    # Accept file name from user
    filename = input("Enter the file name (e.g., textfile.txt): ")
    
    try:
        # (a) Display the first N lines of the file
        n = int(input("Enter the number of lines to display: "))
        print(f"\n--- Displaying first {n} lines ---")
        
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line: # Break if end of file is reached before N lines
                    break 
                print(line.strip()) # strip() removes extra newline characters
                
        # (b) Find the frequency of occurrence of a specific word
        search_word = input("\nEnter the word to find its frequency: ").strip()
        word_count = 0
        
        with open(filename, 'r') as file:
            # Read entire content, convert to lowercase for case-insensitive match
            content = file.read().lower() 
            # Split content into a list of words
            words = content.split()
            # Count the occurrences of the search word
            word_count = words.count(search_word.lower())
            
        print(f"The word '{search_word}' occurs {word_count} times in the file.")
        
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file name.")
    except ValueError:
        print("Error: Please enter a valid integer for the number of lines.")
analyze_file()