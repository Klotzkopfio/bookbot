def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words = get_num_words(text)
    original_text = text
    cleaned_text = exclude_special_chars(original_text)
    counted_characters =  count_characters(cleaned_text)
    chars_sorted_list = chars_dict_to_sorted_list(counted_characters)
    print(f"-- Facts about the text {book_path}--")
    print(f"The counted number of words is {words}.")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times.")

    print("--- End report ---")

def get_text(book_path):
    with open("books/frankenstein.txt") as f:
       file_content = f.read()
       return file_content

def get_num_words(text):
    words = text.split()
    return len(words)  

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def exclude_special_chars(text):
    filtered_text = filter(str.isalpha, text)
    return ''.join(filtered_text)


def count_characters(cleaned_text): 
    chars = {}
    for c in cleaned_text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return dict(sorted(chars.items()))

def sort_on(counted_characters):
    return counted_characters["num"]

main()