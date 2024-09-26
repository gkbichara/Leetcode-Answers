class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        i = 0
        n = len(s)


        while i < n:
            # Check for subtractive combination
            if i < n - 1 and (values[s[i]] < values[s[i + 1]]):
                count += values[s[i + 1]] - values[s[i]]
                i += 2  # Skip the next character as it's part of the combination
            else:
                count += values[s[i]]
                i += 1


        return count