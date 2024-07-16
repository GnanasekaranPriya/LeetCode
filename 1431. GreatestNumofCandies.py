# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        final = []
        for i in range(0,len(candies)): 
            total = candies[i] + extraCandies
            print(total)
            if total >= max_value: 
                final.append(True)
            else:
                final.append(False)
        return final
            

           
            