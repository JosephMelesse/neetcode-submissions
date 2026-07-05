import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int, s=None, e=None) -> List[List[int]]:
        if s is None and e is None:
            s = 0 
            e = len(points) - 1
        if (e - s) + 1 <= 1:
            return points[:k]
        left = s
        pivot = points[e]
        pivot_d = pow(pivot[0], 2) + pow(pivot[1], 2) 
        for i in range(s, e):
            d = pow(points[i][0], 2) + pow(points[i][1], 2)
            if pivot_d > d:
                points[left],points[i] = points[i], points[left]
                left += 1
        points[e], points[left] = points[left], points[e]
        if k == left:
            return points[:k]
        elif k > left:
            return self.kClosest(points, k, left+1, e)
        else:
            return self.kClosest(points, k, s,left-1)

