class Solution:
    def isValid(self, s: str) -> bool:
        #time n
        #space n
        isValid=True
        stack=[]
        for i in s:
            if i =='[' or i =='{' or i =='(':
                stack.append(i)
            elif i ==']'and len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            elif i =='}'and len(stack)!=0 and stack[-1] =='{':
                stack.pop()
            elif i ==')'and len(stack)!=0 and stack[-1] =='(':
                stack.pop()
            else:
                isValid=False
                break;
        if len(stack)!=0:
            isValid=False

        return isValid


            
        