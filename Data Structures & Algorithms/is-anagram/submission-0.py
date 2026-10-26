class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = dict()
        for x in s:
            if x in seenS:
                seenS[x] += 1
            else:
                seenS[x] = 1
        seenT = dict()
        for y in t:
            if y in seenT:
                seenT[y] += 1
            else:
                seenT[y] = 1
        if seenS == seenT:
            return True
        else:
            return False