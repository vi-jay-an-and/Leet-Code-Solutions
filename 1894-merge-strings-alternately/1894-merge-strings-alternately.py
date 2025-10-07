class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) >= len(word2):
            word_max_len = len(word1)
        else:
            word_max_len = len(word2)
        answer = []
        for i in range(word_max_len):
            if i < len(word1):
                answer.append(word1[i])
            if i < len(word2):
                answer.append(word2[i])
        return ''.join(answer)