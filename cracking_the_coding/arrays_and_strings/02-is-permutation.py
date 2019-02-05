# Determine whether or not one string is a permutation of another.


def is_permutation(str1, str2):
    counter_dict = {}
    for char in str1:
        if char in counter_dict:
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1

    print(counter_dict)

    for char in str2:
        if char in counter_dict:
            counter_dict[char] -= 1
        else:
            counter_dict[char] = 1
    print(counter_dict)

    for key in counter_dict:
        if counter_dict[key] > 0:
            return False
    return True


if __name__ == "__main__":
    string1 = input("Enter the string1:")
    string2 = input("Enter the string2:")
    print(is_permutation(string1, string2))