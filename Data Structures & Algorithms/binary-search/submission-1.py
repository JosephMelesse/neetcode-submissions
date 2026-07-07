class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        M = (R+L)//2
        while L < R:
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M+1
                M = (R+L)//2
            elif nums[M] > target:
                R = M-1
                M = (R+L)//2
        if (L == R) and (nums[L] == target):
            return L
        return -1
                
