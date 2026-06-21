class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for c in range(len(s)-1):
            ans += abs(ord(s[c]) - ord(s[c+1]))
        return ans