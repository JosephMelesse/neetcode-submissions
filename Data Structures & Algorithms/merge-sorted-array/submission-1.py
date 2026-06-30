class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        L = nums1[0:m]
        R = nums2
        i = 0
        j = 0
        k = 0
        while len(L) > i and len(R) > j:
            if L[i] <= R[j]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1
            k += 1
        while len(L) > i:
            nums1[k] = L[i]
            k += 1
            i += 1
        while len(R) > j:
            nums1[k] = R[j]
            k += 1
            j += 1