class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        array1 = []
        for i in s:
            array1.append(i)

        array2 = []
        for i in t:
            array2.append(i)
        
        l = 0
        r = 0

        while l < len(array1):
            if r == len(array2):
                return False

            if array1[l] == array2[r]:
                l += 1
                r += 1
                continue

            if array1[l] != array2[r]:
                r += 1
                continue
            
            

        return True

