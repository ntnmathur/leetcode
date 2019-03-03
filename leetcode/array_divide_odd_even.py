# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for elem in A:
            if elem%2 == 0:
                even.append(elem)
            else:
                odd.append(elem)
        return even + odd


A = [3,1,2,4]
print(Solution().sortArrayByParity(A))