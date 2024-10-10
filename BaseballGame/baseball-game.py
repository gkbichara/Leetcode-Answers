class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        answer = []
        n = len(operations)

        for i in range(n):
            if operations[i] == 'C':
                answer.pop()
            elif operations[i] == 'D':
                answer.append(answer[-1] * 2)
            elif operations[i] == '+':
                answer.append(answer[-1] + answer[-2])
            else:
                answer.append(int(operations[i]))
            
        total = 0
        for i in answer:
            total += i

        return total
    