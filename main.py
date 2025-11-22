import sys
from stats import get_book_text, sorted_dic, get_num_words
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
book = get_book_text(path)
dic = sorted_dic(book)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for d in dic:
        print(f"{d}: {dic[d]}")
    print("============= END ===============")
main()