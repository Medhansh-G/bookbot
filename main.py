import sys
from stats import return_num_words, return_num_chars, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        # print(f.read())
        return f.read()

def main():
    try: 
        path_to_book = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frankenstein = get_book_text(path_to_book)
    # print(type(frankenstein))
    # print(return_num_words(frankenstein))
    sorted_dict = return_num_chars(frankenstein)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f'Found {return_num_words(frankenstein)} total words')
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if (dict["letter"].isalpha()):
            print(f'{dict["letter"]}: {dict["count"]}')



    # print(sort_dict)

if __name__ == '__main__':
    main()