class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = {}
        for num in nums:
            if num not in foo:
                foo[num] = 1
            else:
                return True
        return False
            
        