class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        
        start = 0
        count = 1
        i = 1
        while i < len(chars):
            if chars[i] != chars[i-1]:
                if count > 1:
                    temp = list(str(count))
                    for el in temp:
                        chars[start+1] = el
                        start += 1
                    del chars[start+1:i]
                    start += 1
                    i = start
                else:
                    start = i
                i += 1
                count = 1
            else:
                count += 1
                i += 1
        
        if count > 1:
            temp = list(str(count))
            for el in temp:
                chars[start+1] = el
                start += 1
            del chars[start+1:]
                
        return len(chars)


    def compress2(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        
        index = 0
        prev = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != prev:
                chars[index] = prev
                index += 1
                if count > 1:
                    temp = list(str(count))
                    for el in temp:
                        chars[index] = el
                        index += 1
                prev = chars[i]
                count = 1
            else:
                count += 1
                
        chars[index] = prev
        index += 1
        if count > 1:
            temp = list(str(count))
            for el in temp:
                chars[index] = el
                index += 1
        
        del chars[index:]
        return index
                    
        