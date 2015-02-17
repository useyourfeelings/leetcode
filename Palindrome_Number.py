class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        s = 10
        while int(x / s):
            s *= 10
            
        s /= 10
        e = 1
        while s > e:
            if (int(x / s) % 10) != (int(x / e) % 10):
                return False
            s /= 10
            e *= 10
        return True
