class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, m = 0, len(flowerbed)
        while i < m and n > 0:
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == m-1) or (flowerbed[i+1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2  # skip the next plot
                    continue
            i += 1
        return n <= 0