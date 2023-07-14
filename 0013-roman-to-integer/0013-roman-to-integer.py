class Solution:
    def romanToInt(self, s: str) -> int:
      #   str_list = list(s)
        roman = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
      #   answer = roman[str_list[-1]]
      # # 뒤에 나오는 로만 숫자가 더 클 때 str_list[idx+1] - str_list[idx] 
      # # 원래는 str_list[idx] + str_list[idx+1]
      #   for idx,k in enumerate(str_list[:-1]):
      #       if roman[k] < roman[str_list[idx+1]]:
      #           answer -= roman[k]
      #       else:
      #           answer += roman[k]   
      #   return answer
    
    
      # 1. string 도 index로 접근 가능
      # 2. 마지막 문자는 무조건 더하기  
        tot = roman[s[-1]]
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                tot -= roman[s[i]]
            else:
                tot += roman[s[i]]
        return tot