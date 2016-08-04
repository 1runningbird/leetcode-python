# coding: utf8


class Solution(object):
    '''
    Given an integer, write a function to determine if it is a power of two.
    '''
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            n /= 2.0
        if n == 1:
            return True
        return False
