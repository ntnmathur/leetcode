# Missing element between 2 arrays


def finder(arr1, arr2):
    hash_map = {}
    for elem in arr1:
        if elem in hash_map:
            hash_map[elem] += 1
        else:
            hash_map[elem] = 1

    print(hash_map)

    for elem in arr2:
        if elem in hash_map:
            hash_map[elem] -= 1
        else:
            pass

    print(hash_map)

    for k in hash_map:
        if hash_map[k] > 0:
            return k
    return 0


arr1 = [5,5,7,7]
arr2 = [5,7,7]

print(finder(arr1,arr2))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):

    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)