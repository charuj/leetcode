'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5

Input: [7,6,4,3,1]
Output: 0


'''

import unittest

class Solution:
    def maxprofit(self, prices):
        # traverse the list left to right
        # two pointers: one for min price, one for max
        # if max > min, return difference as max profit

        max_price= prices[0]
        min_price= prices[0]

        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price= prices[i]
                max_price= prices[i]

            if prices[i] > max_price:
                max_price = prices[i]

        return (max_price - min_price)



class TestSolution(unittest.TestCase):
    def testmaxprices(self):
        sol= Solution()
        profit= sol.maxprofit([7,1,5,3,6,4])
        self.assertEqual(profit, 5)
    def testmaxprices2(self):
        sol= Solution()
        profit= sol.maxprofit([7,6,4,3,1])
        self.assertEqual(profit, 0)


if __name__ == "__main__":
    unittest.main()


