class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      # print(word[0])
      # print(word[1:])
      # print(word[1:])
      if word[0].isupper() == True:
        if word[1:].lower() == word[1:]: # Google
          return True 
        elif word[1:].upper() == word[1:]: # USA
          return True 
        else:
          return False
      elif word[1:].lower() == word[1:]: # leetcode
        return True 
      else:
        return False