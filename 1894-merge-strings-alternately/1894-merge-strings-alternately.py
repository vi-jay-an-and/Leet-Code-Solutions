class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        result = [word1[i] + word2[i] for i in range(min_len)]
        result = result + list(word1)[min_len:] + list(word2)[min_len:]
        return ''.join(result)