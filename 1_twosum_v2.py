'''
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
'''
import unittest

class Solution(object):
    def two_sum(self, nums, target):
        #Go through the list of nums, and add corresponding (target - num) & index to dict

        self.seen_dict={}
        for i in range(len(nums)):
            tmp= target - nums[i]
            if tmp not in self.seen_dict:
                self.seen_dict[tmp]=i
            if nums[i] in self.seen_dict:
                return [self.seen_dict[nums[i]], i]





class TestSolution(unittest.TestCase):
    def test_dict(self):
        ts= Solution()
        ts1= Solution()
        ts.two_sum(nums= [2,7], target=9)
        ts1.two_sum(nums= [2,-7], target=9)
        sd= ts.seen_dict
        sd1= ts1.seen_dict
        self.assertEqual(sd, {7:0, 2:1})
        self.assertEqual(sd1, {7:0, 16:1})

    def test_sol(self):
        ts= Solution()
        ans= ts.two_sum(nums=[2,7,11,15], target=9)
        ans1= ts.two_sum(nums=[-5,-10,0,9, 7,17,1], target=9)
        self.assertEqual(ans, [0,1])
        self.assertEqual(ans1, [2,3])


if __name__ == "__main__":
    unittest.main()
