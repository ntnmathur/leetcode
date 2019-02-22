# https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20SOLUTIONS/Anagram%20Check%20-%20SOLUTION.ipynb#Anagram-Solution


# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
#
# For example:
#
# "public relations" is an anagram of "crap built on lies."
#
# "clint eastwood" is an anagram of "old west action"

from nose.tools import assert_equal

def anagram2(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)


def anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    counts = {}
    for elem in s1:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    for elem in s2:
        if elem in counts:
            counts[elem] -= 1
        else:
            counts[elem] = 1

    for k in counts:
        if counts[k] != 0:
            return False
    return True

class AnagramTest(object):

    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")


if __name__ == '__main__':
    print(anagram('dog','god'))
    print(anagram('clint eastwood','old west action'))
    print(anagram2('dd','aa'))
    t = AnagramTest()
    t.test(anagram)
