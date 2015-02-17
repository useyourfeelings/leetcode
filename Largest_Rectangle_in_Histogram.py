class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        length = len(height)
        records = []#[starting_pos, height]
        result = 0
        
        for i in range(length):
            start = i
            while len(records) and height[i] < records[-1][1]:
                record = records.pop()
                start = record[0]
                area = record[1] * (i - record[0])
                if result < area:
                    result = area
            
            records.append([start, height[i]])
            
        for record in records:
            area = record[1] * (length - record[0])
            if result < area:
                result = area
        
        return result
