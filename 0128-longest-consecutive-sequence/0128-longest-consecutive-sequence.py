class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = list(set(nums))
        result.sort()
        sequence = [1] * len(result)
        seq_no = 0
        for i in range(1,len(result)):
            if ((result[i] - result[i-1] - 1 ) == 0):
                sequence[seq_no] += 1
            else:
                seq_no += 1
        return max(sequence)