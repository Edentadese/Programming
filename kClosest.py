class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            sq=(points[i][0])*(points[i][0])+(points[i][1])*(points[i][1])
            points[i].insert(0,sq)
    
        points.sort(key = lambda x: x[0])
      

        for i in range(len(points)):
            del points[i][0]
    
        res=[]
    
        for j in range(k):
            res.append(points[j])
        return res
        
