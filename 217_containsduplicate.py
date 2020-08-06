'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''

#Option 1: use set(), O(N) time complexity
#Option 2: use hash to track seen



import unittest


class Solution:
    def hasDuplicate(self, nums):
        #iterate through the list
        #initialize a hash
        # if element not in hash, add
        # if in hash, return True

        self.seen={}
        for i in nums:
            if i not in self.seen:
                self.seen[i]=1
            else:
                return True
        return False



class TestSolution(unittest.TestCase):
    def test1(self):
        nums= [1,2,3,1]
        sol= Solution()
        ans= sol.hasDuplicate(nums)
        self.assertEqual(ans, True)

    def test2(self):
        nums= [1,2,3,4]
        sol= Solution()
        ans= sol.hasDuplicate(nums)
        self.assertEqual(ans, False)

    def test3(self):
        nums=  [1,1,1,3,3,4,3,2,4,2]
        sol= Solution()
        ans= sol.hasDuplicate(nums)
        self.assertEqual(ans, True)


if __name__ == "__main__":
    unittest.main()
