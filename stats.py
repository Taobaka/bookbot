def print_book_path(path):
    print(f"The path is: {path}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(path_to_book):
    text = get_book_text(path_to_book)
    words = text.split()
    word_amount = len(words)
    return word_amount

def symbol_count(path_to_book):
    symbol_dict={}
    text = get_book_text(path_to_book)
    for i in text.lower():
        if i in symbol_dict:
            symbol_dict[i] += 1
        else:
            symbol_dict[i] = 1
    return symbol_dict

def sort_prio(symbol_dict):
    return symbol_dict["num"]

def test(symbol_dict):
    list_of_dictionaries=[]
    for char, count in symbol_dict.items():
        if char.isalpha():
            list_of_dictionaries.append({"char": char, "num": count})
    list_of_dictionaries.sort(reverse=True,key=sort_prio)
    return list_of_dictionaries

