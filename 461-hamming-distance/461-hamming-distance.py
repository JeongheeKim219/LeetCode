class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            print('x :', x)
            print('y :', y)
            if x%2 != y%2:
                cnt += 1
            x, y = x//2, y//2
            
        return cnt