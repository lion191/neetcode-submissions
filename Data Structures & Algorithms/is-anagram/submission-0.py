class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        arranges = sorted(s)
        arranget = sorted(t)
        if(arranges == arranget):
          return True
        else: 
          return False
        