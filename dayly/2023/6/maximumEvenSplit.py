class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        if finalSum % 2 != 0:
            return res
        i = 2
        while finalSum >= 2 * i + 2:
            res.append(i)
            finalSum -= i
            i += 2

        res.append(finalSum)
        return res
