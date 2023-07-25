class Solution:       
    def plusOne(self, digits) :
      num = "" 
      for i in digits:
        num += str(i)
      answer = [int(i) for i in str(int(num)+1)]
      return answer