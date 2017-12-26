# Assignment 4.2

def len_word(wdlist):
    lenlist = []
    for wd in wdlist:
        lenlist.append(len(wd))
    return lenlist

input_list = ['one','two','three','four']
print(len_word(input_list))

def is_vowel(str1):
    vowel_set = {'a','e','i','o','u'}    
    if str1 in vowel_set:       
        return True
    else:
        return False
    
print(is_vowel('b'))
print(is_vowel('e'))