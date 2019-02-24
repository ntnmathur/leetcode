def reverse_word(word):
    word_len = len(word)-1
    rev = []
    while word_len >=0:
        rev.append(word[word_len])
        word_len -=1
    return ''.join(rev)


def reverse_sentence(sentence):

    sentence_list = sentence.split(' ')
    reverse_sentence_list = []
    sen_len = len(sentence_list)-1
    while sen_len >=0:
        if sentence_list[sen_len] != '':
            reverse_sentence_list.append(sentence_list[sen_len])
        sen_len -= 1

    return ' '.join(reverse_sentence_list)


print(reverse_sentence('   Hello John    how are you   '))
print(reverse_sentence('    space before'))

from nose.tools import assert_equal

class ReversalTest(object):

    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")

# Run and test
t = ReversalTest()
t.test(reverse_sentence)
