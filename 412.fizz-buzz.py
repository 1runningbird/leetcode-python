# coding: utf8
class Solution(object):
    '''
    Write a program that outputs the string representation of numbers from 1 to n.
    But for multiples of three it should output “Fizz” instead of the number and for
    the multiples of five output “Buzz”.
    For numbers which are multiples of both three and five output “FizzBuzz”.
    '''
    def convert(self, num):
        if num % 15 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        return str(num)

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [self.convert(i+1) for i in xrange(n)]
