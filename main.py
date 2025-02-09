def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        results = char_count(file_contents)
        count = word_count(file_contents)
        char_list = dict_to_sorted_list(results)

        # print(char_list)


        print(f"--- Begin report of {f.name} ---")
        print(f"{count} words found in the document\n")
        
        for char in char_list:
            print(f"The '{char["char"]}' character was found {char["count"]} times")
        
        print('--- End report ---')

# converts a dictionary of all characters and their counts to individual dictionaries in a list and sorts them highest to lowest
def dict_to_sorted_list(dict):

    def sort_on(dict):
        return dict["count"]

    dict_list = []
    
    for char in dict:
        dict_list.append(
            {"char": char, "count": dict[char]}
        )
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list

# returns the total count of words in the document
def word_count(text):
    word_list = text.split()
    
    return len(word_list)

# returns the count of each instance of alphabetical characters
def char_count(text):
    lowercase_text = text.lower()

    char_count_dict = {}

    for char in lowercase_text:
        if char.isalpha() == True:
             char_count_dict[char] = 0
            
    for char in lowercase_text:
        if char.isalpha() == True:
            char_count_dict[char] += 1

    return char_count_dict

main()