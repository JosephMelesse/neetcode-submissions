class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            checked[numbers[i]] = i
            if complement in checked and complement != numbers[i]:
                print(checked, checked[complement], i)
                
                return [checked[complement] + 1 , i + 1 ]