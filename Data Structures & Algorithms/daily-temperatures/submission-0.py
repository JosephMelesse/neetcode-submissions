class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for t in temperatures]
        for i in range(len(temperatures)):
            if i==0:
                stack.append(i)
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                popped_i = stack.pop()
                answer[popped_i] = i - popped_i
            stack.append(i)
        return answer




        