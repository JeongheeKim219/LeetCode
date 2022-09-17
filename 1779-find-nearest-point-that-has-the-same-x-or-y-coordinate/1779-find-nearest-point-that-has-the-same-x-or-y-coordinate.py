class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dic = dict()
        for idx, val in enumerate(points, start=0):
            a, b = val
            if a == x or b == y:
                dic[idx] = abs(x-a) + abs(y-b)
            
        v_ls = list(dic.values())        
        if len(v_ls) == 0:
            return -1
        
        mini = min(v_ls)
        for k, v in dic.items():
            print(k, v)
            if v == mini:
                return k
            