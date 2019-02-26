def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


print(factorial(5))


def rec_sum(n):
    if n == 0:
        return 0
    return n + rec_sum(n-1)


print(rec_sum(5))


# sum of individual digits

def sum_func(n):
    if len(str(n)) == 1:
        return n

    return n%10 + sum_func(n//10)


print(sum_func(123))

# Check if string can be split into words in list


def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output

print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split('manranthe',['clown','ran','man']))



