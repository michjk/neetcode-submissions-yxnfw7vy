class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for num in sorted(count):
            if count[num]:
                amt = count[num]
                for i in range(num, num + groupSize):
                    if count[i] < amt:
                        return False
                    count[i] -= amt
        return True