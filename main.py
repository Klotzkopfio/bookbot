def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words = get_num_words(text)
    print(text)
    print(f"the counted number of words is {words}")

def get_text(book_path):
    with open("books/frankenstein.txt") as f:
       file_content = f.read()
       return file_content

def get_num_words(text):
    words = text.split()
    return len(words)      
 
main()