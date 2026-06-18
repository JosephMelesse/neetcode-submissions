class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        foo = 0
        bar = 0
        for n in nums:
            if n == 1:
                bar += 1
            else:
                if bar > foo:
                    foo = bar
                bar = 0
        return bar if bar > foo else foo  

        