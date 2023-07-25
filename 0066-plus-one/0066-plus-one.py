# class Solution:       
#     def plusOne(self, digits) :
#       num = "" 
#       for i in digits:
#         num += str(i)
#       answer = [int(i) for i in str(int(num)+1)]
#       return answer
class Solution:       
    def plusOne(self, digits) :
      if len(digits) == 1 and digits[0] == 9 :
        return [1,0]
      elif digits[-1] < 9:
        digits[-1] +=1
        return digits
      else: # digits[-1] ==9, len(digits) > 1
        digits[-1] = 0
        digits[0:-1] =self.plusOne(digits[0:-1])
        return digits