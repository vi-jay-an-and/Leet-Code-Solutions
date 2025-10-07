class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        last_index = len(str_list) - 1
        for i in range(0,(len(str_list)//2)):
            str_list[last_index-i],str_list[i] = str_list[i], str_list[last_index-i]
        return ' '.join(str_list)