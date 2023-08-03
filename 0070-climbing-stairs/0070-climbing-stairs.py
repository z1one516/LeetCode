# class Solution:
#     def climbStairs(self, n: int) -> int:
def factorial(num):
        fact = 1
        if num == 0 or num == 1:
            return 1
        else: 
            return num * factorial(num-1)

class Solution:
    def climbStairs(self, n):
        answer = 1
        div_2 = n//2
        mod_2 = n%2
    
        if div_2 == 0:
            pass
        else:
            if mod_2 == 0:
                split_2 = div_2
                for num in range(div_2, div_2*2): 
                    plus = factorial(num) / (factorial(split_2)*factorial(num-split_2) )

                    split_2 -= 1
                    answer += plus
            else:
                split_2 = div_2 
                for num in range(div_2+1, div_2*2+1): 
                    plus = factorial(num) / (factorial(split_2)*factorial(num-split_2))
                    split_2 -= 1
                    answer += plus
        return int(answer)
        