# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

class Solution:
    def strStr(self, haystack, needle):
        answer = -1
        n_len = len(needle)
        h_len = len(haystack)
        idx = 0
        while h_len:
            # needle 한 글자
            if n_len == 1:
                answer = idx if needle in haystack else answer
            
            # 종료 조건
            if h_len ==1:
                if haystack == needle:
                    answer = 0
                return answer
            
            # 같은 단어가 있는지 확인
            if haystack[idx:idx+n_len] == needle:
                answer = idx
                return answer
            idx +=1
            h_len -=1
        