def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        re = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                re += roman[s[i]]
            elif (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                re += roman[s[i+1]] - roman[s[i]]
                i += 1
            else:
                re += roman[s[i]]
            i += 1

        return re

def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        re = 0
        prev = 0
        for el in reversed(s):
            num = roman[el]
            if num < prev:
                re -= num
            else:
                re += num
            prev = num
            
        return re