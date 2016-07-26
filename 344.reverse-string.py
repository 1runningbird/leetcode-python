# coding: utf8


class Solution(object):
    '''
    Write a function that takes a string as input
        and return the reversed.
    '''
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    s = Solution()
    ss = 'hello'
    sss = s.reverseString(ss)
    print 'before %s' % ss
    print 'after reverse %s' % sss
