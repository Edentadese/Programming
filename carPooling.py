class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1000
        for i in range(len(trips)):
            for j in range(trips[i][1],trips[i][2]):
                arr[j] += trips[i][0]
                if (arr[j] > capacity):
                    return False;



        return True
        
