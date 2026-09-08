class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        res = []
        for i in range(k):
            max_k = float("-inf")
            max_v = float("-inf")
            for key in freq:
                if freq[key] > max_v:
                    max_v = freq[key]
                    max_k = key
            freq.pop(max_k)
            res.append(max_k)
        return res

        