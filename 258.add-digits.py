# coding: utf8


class Solution(object):
    '''
    Given a non-negative integer num, repeatedly add all
        its digits until the result has only one digit.

    For example:

    Given num = 38, the process is like: 3 + 8 = 11,
        1 + 1 = 2. Since 2 has only one digit, return it.

    TODO
    Follow up:
    Could you do it without any loop/recursion in O(1) runtime?
    '''
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = sum([int(i) for i in str(num)])
        if s >= 10:
            return self.addDigits(s)
        return s


if __name__ == '__main__':
    solution = Solution()
    print solution.addDigits(100)
