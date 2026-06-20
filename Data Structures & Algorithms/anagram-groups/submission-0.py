from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for i in strs:
            key = tuple(sorted(i))
            l[key].append(i)
        return list(l.values())