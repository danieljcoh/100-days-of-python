class Solution(object):
    def reverse(self, x):
        
        NEGATIVE_INT = int(-2.147483647e9) + 1
        POSITIVE_INT = int(2.147483647e9) - 1 
        multiplier = 1
    
        if x < 0:
            multiplier = -1
        
        final_array = []
        x = str(x)
        x_list = list(x)
        if multiplier == -1:
            x_list.pop(0)
        for str_char in range(len(x_list) - 1, -1, -1):
            final_array.append(x_list[str_char])
        x = int(''.join(final_array))
        x *= multiplier
        if x < POSITIVE_INT:
            if x < NEGATIVE_INT:
                return 0
            return x
        elif x > NEGATIVE_INT: 
            if x > POSITIVE_INT:
                return 0
            return x
        return 0