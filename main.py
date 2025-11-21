from stats import sorted_dic, get_num_words
dic = sorted_dic()
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    for d in dic:
        print(f"{d}: {dic[d]}")
    print("============= END ===============")
main()