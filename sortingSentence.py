class Solution:
    def sortSentence(self, s: str) -> str:
        arrStr = s.split()
        final = [0] * len(arrStr)
        for arr in arrStr:
            final[int(arr[-1]) - 1] = arr[:-1]
        return ' '.join(final)