class Solution:
    def isPalindrome(self, s: str) -> bool:
        #case insensitive A=a 
        #only a-z and 0-9 no spaces 
        #condition: if valid char [i]!=valid char [j] return false
        #if invalid char, skip i++ or j--
        #if i==j then stop
       
        t = ''
        for c in s:
            if c.isalnum():
                t+=c
        t=t.lower()
        print(t)

        i,j=0, len(t)-1

        if j<0:
            return True

        while i<j:
            if t[i]!=t[j]:
                return False
            i+=1
            j-=1
        return True


        