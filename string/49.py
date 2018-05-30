def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = {}
        
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in dic:
                dic[temp] = []
            dic[temp].append(s)
            
        return [dic[el] for el in dic]