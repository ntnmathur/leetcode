# Determine whether or not a given string contains no duplicate characters.

def contains_no_duplicates(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = True
    return True


if __name__ == "__main__":
    import sys
    string = input("Enter the string:")
    print(contains_no_duplicates(string))

