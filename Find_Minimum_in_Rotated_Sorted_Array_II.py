class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        left = 0
        right = len(num) - 1
        center = 0
        
        while True:
            if right - left <= 1:
                return min(num[left], num[right])
                
            center = (left + right) / 2
            
            if num[left] > num[center]:
                right = center
                continue
            elif num[center + 1] > num[right]:
                left = center + 1
                continue
            elif num[left] == num[center] or num[center + 1] == num[right]:
                result = num[left]
                for i in range(left + 1, right + 1):
                    if result > num[i]:
                        result = num[i]
                return result
            else:
                return min(num[center + 1], num[left])
