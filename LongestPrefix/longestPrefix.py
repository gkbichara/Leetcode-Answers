class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs[0] == "":
            return ""
        prefix = strs[0]

        for i in strs:
            if i == "":
                return ""
            else:
                n = len(i)
                m = len(prefix)
                range_needed = min(m, n)
                temp_prefix = ""
                for j in range(range_needed):
                    if i[j] == prefix[j]:
                        temp_prefix += prefix[j]
                    else:
                        prefix = prefix[:j]
                        break
                
                prefix = temp_prefix
            
        return prefix