def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

book = get_book_text("books/frankenstein.txt")
def get_num_words():
    lists_book = book.split()
    return len(lists_book)

def dictionary():
    d = {}
    for b in book:
        if not b.isalpha():
            continue
        lower = b.lower()
        if lower not in d:
            d[lower] = 1
        elif lower in d:
            d[lower] += 1
    return d

def sort_on(items):
    return items[1]

def sorted_dic():
    d = sorted(dictionary().items(),           
    key=sort_on,
    reverse=True              
    )
    return dict(d)

            
    