def return_num_words(string):
    num_words = len(string.split())
    # return (f'{num_words} words found in the document')
    return num_words

def return_num_chars(string):
    words = list(string)

    for i in range(len(words)):
        word = words[i]
        word = word.lower()
        words[i] = word
    
    count_per_letter = {}
    for letter in words:
        if letter in count_per_letter:
            cur_count = count_per_letter[letter]+1
            count_per_letter[letter]=cur_count
        else:
         count_per_letter[letter] = 1
         
    return sort_dict(count_per_letter)

def sort_on(count_dict):
    return count_dict['count']

def sort_dict(count_dict):
    sorted_list = []
    for letter in count_dict:
        letter_dict = {"letter":  letter, "count": count_dict[letter]}
        sorted_list.append(letter_dict)
        # print(count_dict[letter])
    # print(sorted_list)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
return_num_chars("The quick brown fox jumps over the lazy dog")