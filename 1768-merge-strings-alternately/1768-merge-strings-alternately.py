class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_merged = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                word_merged += word1[i]
                word_merged += word2[i]
            for i in range(len(word2),len(word1)):
                word_merged += word1[i]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                word_merged += word1[i]
                word_merged += word2[i]
            for i in range(len(word1),len(word2)):
                word_merged += word2[i]
        else:
            for i in range(len(word1)):
                word_merged += word1[i]
                word_merged += word2[i]
        
        return word_merged