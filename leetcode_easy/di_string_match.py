

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        num_i = S.count("I")
        num_d = S.count("D")
        for char in S:
            if char == "I":
                output.append(curr_val+)