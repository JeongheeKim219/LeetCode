class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mini = 214700000
        index = -1
        for idx, val in enumerate(points, start=0):
            a, b = val
            if a == x or b == y:
                dis = abs(x-a) + abs(y-b)
                if mini > dis:
                    mini = dis
                    index = idx
        return index