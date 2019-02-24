# There is an array and a number. Find how many pairs within the array add up to the number


def pair_sum(arr, k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)  # hold the number if target is not seen before
        else:
            output.add((num,target))

    return len(output)

from nose.tools import assert_equal

class TestPair(object):

    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')

#Run tests
t = TestPair()
t.test(pair_sum)

