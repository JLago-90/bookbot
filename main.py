def number_of_words(book_string):
    words = book_string.split()
    return len(words)

def character_count(book_string):
    char_count = {}
    lower_letters = book_string.lower()

    for key in lower_letters:
        if key in char_count:
            char_count[key] += 1
        else:
            char_count[key] = 1

    return char_count

def letters_list(dict):
    list_of_dict = []

    for key, value in dict.items():
        if key.isalpha():
            temp_dict = {}
            temp_dict["char"] = key
            temp_dict["count"] = value
            list_of_dict.append(temp_dict)
        
    def sort_on(dict):
        return dict["count"]
    
    list_of_dict.sort(reverse=True, key=sort_on)


    return list_of_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
       
        num_words = number_of_words(file_contents)
        char_count = character_count(file_contents)
        ordlista = letters_list(char_count)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        print()
        
        for bokstav in ordlista:
            print(f"The '{bokstav['char']}' character was found {bokstav['count']} times")

        print("--- End report ---")

if __name__ == "__main__":
    main()
