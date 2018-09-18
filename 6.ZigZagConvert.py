# apporoach visit by row
class Solution:
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if num_rows == 1:
            return s
        
        result = str()
        group_size = 2 * num_rows - 2
        
        for i in range(num_rows):
            visitor = i
            
            while visitor < len(s):
                result += s[visitor]
                
                if i != 0 and i != num_rows - 1:
                    speical_visitor = visitor + group_size - 2 * i
                    
                    if speical_visitor < len(s):
                        result += s[speical_visitor]
                            
                visitor += group_size
                
        return result
        
            