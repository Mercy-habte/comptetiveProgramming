class Solution:
    def sortSentence(self, s: str):
        s = s.split(" ")
        final_sen = ""
        for i in range (len(s)):
            min_index = i
            for j in range(i+1, len(s)):
                if s[j][-1] < s[min_index][-1]:
                    min_index = j
            if i != min_index:
                s[min_index], s[i] = s[i], s[min_index]
            final_sen += s[i][:-1] + ' '
        return (final_sen[:-1])
            