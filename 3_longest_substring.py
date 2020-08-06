"Given a string, find the length of the longest substring without repeating characters."
import unittest

class Solution(object):
    #Sliding window?
    # Go through the list, element by element
    # Use a dictionary to track whether you've seen the char before
    # if not seen: add to the dictionary
    # if seen: move the start of the substring to that index
    # simulaneously, track length of longest substring

    def longest(self, lstring):
        # Go through string and check that haven't encountered the character before

        self.seen_dict={}
        maxlen= 0
        tmp= 0
        for s in lstring:
             if s not in self.seen_dict:
                self.seen_dict[s]=1
                tmp +=1

            else:

                # flush dictionary
                # compare tmp and maxlen for which is greater
                # reset tmp to zero
                self.seen_dict={}
                self.seen_dict[s]= 1

                if tmp > maxlen:
                    maxlen = tmp
                    tmp=1
        return maxlen


class TestSolution(unittest.TestCase):
    def testdict(self):
        sol= Solution()
        _= sol.longest("abc")
        self.assertEqual(sol.seen_dict, {"a":1, "b": 1, "c":1})
        _= sol.longest("abcbbb")
        self.assertEqual(sol.seen_dict, {"b": 1})

    def testsol(self):
        sol= Solution()
        maxlen= sol.longest("abcabcbb")
        self.assertEqual(maxlen, 3)
        maxlen= sol.longest("bbbbb")
        self.assertEqual(maxlen, 1)
        maxlen= sol.longest("pwwkew")
        self.assertEqual(maxlen, 3)


if __name__ == "__main__":
    unittest.main()


