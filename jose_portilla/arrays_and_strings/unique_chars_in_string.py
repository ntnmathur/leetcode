def is_unique(string):
    chars_set = set()
    for char in string:
        if char in chars_set:
            return False
        else:
            chars_set.add(char)
    return True


from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestUnique()
t.test(is_unique)