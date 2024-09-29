class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        answer = []
        counter = 0
        temp = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if temp == nums[i - 1]:
                    answer.append(str(temp))
                else:
                    answer.append("{}->{}".format(temp, nums[i - 1]))
                temp = nums[i]

        if temp == nums[-1]:
            answer.append(str(temp))
        else:
            answer.append("{}->{}".format(temp, nums[-1]))

        return answer

