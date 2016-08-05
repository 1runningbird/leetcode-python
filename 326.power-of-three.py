# coding: utf8


class Solution(object):
    '''
    Given an integer, write a function to determine if it is a power of three.
    '''
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 3:
            n /= 3.0
        if n == 1:
            return True
        return False
