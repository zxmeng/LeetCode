def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        if not envelopes or not envelopes[0]:
            return 0
        
        envelopes.sort()
        
        dup_count = 1
        for i in range(1, len(envelopes)):
            if envelopes[i][0] == envelopes[i-1][0]:
                dup_count += 1
            elif dup_count != 1:
                envelopes[i-dup_count:i] = reversed(envelopes[i-dup_count:i])
                dup_count = 1

        if dup_count != 1:
            envelopes[-dup_count:] = reversed(envelopes[-dup_count:])
        
        re = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > re[-1]:
                re.append(envelopes[i][1])
            else:
                left = 0
                right = len(re) - 1
                while left <= right:
                    mid = int((left+right)/2)
                    if re[mid] >= envelopes[i][1]:
                        right = mid - 1
                    else:
                        left = mid + 1
                re[left] = envelopes[i][1]
        
        return len(re)