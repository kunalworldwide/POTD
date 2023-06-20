class Solution:
    def matchGame(self, N):
         # code here
        if N % 5 == 0:
            return -1
        for i in range(0,5):
            c=N-i
            if c % 5 == 0:
                return i
        return -1
