class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            a = i % 3
            b = i % 5
            if not a and not b:
                res.append('FizzBuzz')
            elif not a:
                res.append('Fizz')
            elif not b:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res