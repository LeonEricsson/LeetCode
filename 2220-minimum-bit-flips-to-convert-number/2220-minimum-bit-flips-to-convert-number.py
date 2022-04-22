class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        swap = goal^start
        return bin(swap).count('1')