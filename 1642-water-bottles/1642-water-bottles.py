class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            emptyBottles = numBottles % numExchange
            numBottles //= numExchange
            numBottles += emptyBottles
        return res
