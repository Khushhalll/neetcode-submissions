class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        n = len(s)
        for c in range(n-1):
            ans += abs(ord(s[c]) - ord(s[c+1]))
        return ans