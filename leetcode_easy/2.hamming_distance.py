# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        for tups in zip('{0:01000b}'.format(x), '{0:01000b}'.format(y)): # convert number to binary
            if tups[0] != tups[1]:
                distance += 1
        return distance


print(Solution().hammingDistance(1,2))