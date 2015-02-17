class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        phone = {}
        phone['2'] = ['a', 'b', 'c']
        phone['3'] = ['d', 'e', 'f']
        phone['4'] = ['g', 'h', 'i']
        phone['5'] = ['j', 'k', 'l']
        phone['6'] = ['m', 'n', 'o']
        phone['7'] = ['p', 'q', 'r', 's']
        phone['8'] = ['t', 'u', 'v']
        phone['9'] = ['w', 'x', 'y', 'z']
        
        total_num = 1
        for i in range(len(digits)):
            total_num *= len(phone[digits[i]])
        
        result = [""] * total_num
        
        num = total_num
        for i in range(0, len(digits)):
            size = len(phone[digits[i]])
            num /= size
            pick = size - 1
            for j in range(total_num):
                if j % num == 0:
                    pick = (pick + 1) % size
                result[j] += phone[digits[i]][pick]
        
        return result
