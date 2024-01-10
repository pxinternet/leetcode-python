class Solution:

    #典型的动态规划问题
    def numDecoding(self, s:str) -> int:
        n = len(s)

        f = [1] + [0] * n

        for i in range(1, n+1):
            a = int(s[i-1])
            if 1 <= a <= 9:
                f[i] += f[i-1]
            if i > 1:
                b = (int(s[i - 2])) * 10 + a
                if 10 <= b <= 26:
                    f[i] += f[i-2]

        return f[n]
