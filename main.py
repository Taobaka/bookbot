import sys
if len(sys.argv) !=2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
from stats import print_book_path, get_num_words, symbol_count, test

book_path = sys.argv[1]
print_book_path(book_path)

total_word_count=get_num_words(book_path)
end_count = symbol_count(book_path)
result = test(end_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}")
print("----------- Word Count ----------")
print(f"Found {total_word_count} total words")
print("--------- Character Count -------")
for entry in result:
   print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")