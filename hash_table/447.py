def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if len(points) < 3:
            return 0
        
        total = 0
        for i in range(len(points)):
            dist_dict = {}
            for j in range(len(points)):
                dist = (points[j][0] - points[i][0]) ** 2
                dist += (points[j][1] - points[i][1]) ** 2
                if dist not in dist_dict:
                    dist_dict[dist] = 0
                dist_dict[dist] += 1
                
            for el in dist_dict:
                if dist_dict[el] >= 2:
                    total += dist_dict[el] * (dist_dict[el]-1)
                    
        return total