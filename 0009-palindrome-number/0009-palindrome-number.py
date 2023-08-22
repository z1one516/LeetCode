class Solution:
    def isPalindrome(self, x):
      # print('reversed:', ''.join(reversed(str(x))))
      if str(x) == ''.join(reversed(str(x))):
        return True
      else:
        return False
     #  def reverse(string):
     #    string = list(string)
     #    string.reverse()
     #    return "".join(string)
        