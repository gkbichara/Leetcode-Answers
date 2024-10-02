class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        counter = 0

        answers = set(jewels)

        for stone in stones:
            if stone in answers:
                counter += 1
            else:
                continue

        return counter