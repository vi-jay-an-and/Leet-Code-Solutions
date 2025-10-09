class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        result = []
        for i in range(len(candies)):
            max_candies = candies[i] + extraCandies
            if max_candies >= max_val:
                result.append(True)
            else:
                result.append(False)
        return result