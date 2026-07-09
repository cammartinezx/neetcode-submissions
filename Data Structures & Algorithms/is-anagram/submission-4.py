class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #time O(n)+O(n) space O(26 letters)so O(1)

        count={}

        if len(s)!=len(t):
            return False
        #get freq for each char from first string
        for char in s:
            count[char]= count.get(char,0)+1
        
        for char in t:
            if char not in count.keys():
                return False
            count[char]-=1
            if count[char]<0:
                return False
        
        return True


        

        