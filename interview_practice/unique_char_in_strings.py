__author__ = 'jtakwani'
#to check if the strings have unique characters

def check():
    string = 'Jeet'
    string_1 = 'Hriya'
    map = {}
    bool_val_for_string = False
    bool_val_for_string_1 = False
    for i in range(len(string)):
        if string[i] in map:
            bool_val_for_string = True
        map[string[i]] = i

    for i in range(len(string_1)):
        if string_1[i] in map:
            bool_val_for_string_1 = True
        map[string_1[i]] = i

    return (bool_val_for_string, bool_val_for_string_1)

print(check())