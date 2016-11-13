# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# there is exactly one solution

nums= [2, 11, 11,7, 15]
target= 9


class Sol2(object):
    def twosum(self, nums, target):
        '''

        :param nums: list(int)
        :param target: int
        :return: list(int)
        '''

        # the way this soln works:
        # 1) Make a dictionary
        # 2) For each element in the list nums, subtract it from the target, and put this difference in the dictionary
        # 3) If a number in the dictionary is also in the list, return [index of first num, i]
        dic={}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target-num]=i

sol= Sol2()
print sol.twosum(nums, target)