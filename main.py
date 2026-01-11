import sys
from stats import count_words
from stats import count_characters
from stats import list_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:     
        contents = f.read()         
    return contents

def sort_characters(char):
    return char["num"]                         

def main():
    file_path = sys.argv[1]                           # Allow input for file path
    words = get_book_text(file_path)
    word_count = count_words(words)         
    character_count = count_characters(words)
    report = list_characters(character_count)            
    report.sort(reverse=True, key=sort_characters)      
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------""")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in report:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()