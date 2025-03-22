import os
import string

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.strip()
        
        words = text.split()

        return len(words)
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def count_words_in_input_folder():
    input_dir = 'input'
    total_word_count = 0

    if not os.path.exists(input_dir):
        print(f"The directory 'input' does not exist.")
        return

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            try:
                word_count = count_words_in_file(file_path)
                print(f"Word count for {filename}: {word_count}")
                total_word_count += word_count
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    print(f"\nTotal word count for all files: {total_word_count}")

if __name__ == "__main__":
    while True:
        count_words_in_input_folder()
        
        restart = input("\nPress Enter to restart the script, or type 'exit' to quit: ").strip().lower()
        if restart == 'exit':
            print("Exiting the script...")
            break
