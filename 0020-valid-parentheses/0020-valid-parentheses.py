class Solution:
    def isValid(self, s) :
        stack_str = []
        for i in s:
            if (i=='('or i=='{'or i=='['):
                stack_str.append(i)
            else:
                if stack_str == []:
                    return False
                elif i == ')' and stack_str[-1] == '(':
                    stack_str.pop()
                elif i =='}' and stack_str[-1] =='{':
                    stack_str.pop()
                elif i ==']' and stack_str[-1] =='[':
                    stack_str.pop()
                else:
                    return False
        return not stack_str
      