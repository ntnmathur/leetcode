# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        hash_map = {x:0 for x in J}
        for char in S:
            if char in hash_map.keys():
                hash_map[char] += 1
        return sum(hash_map.values())


J = "aA"
S = "aAAbbbb"
print(Solution().numJewelsInStones(J,S))