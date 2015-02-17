class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        length = len(s)
        if length == 0:
            return 0
            
        return len((s.split(' ')[-1].lstrip()))
