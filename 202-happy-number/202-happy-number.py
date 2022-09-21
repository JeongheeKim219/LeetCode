class Solution:
    ls = list()
    def isHappy(self, n: int) -> bool:
        tot = 0
        while n > 0:
            tmp = n%10
            n = n//10
            tot += tmp**2
        self.ls.append(tot)
        
        print(tot)
        print(self.ls)
                
        if tot == 1:
            self.ls.clear()
            return True
        else:
            if tot in self.ls[:-2]:
                return False
            else:
                return self.isHappy(tot)