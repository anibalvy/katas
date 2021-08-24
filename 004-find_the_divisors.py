'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns 
an array with all of the integer's divisors(except for 1 and the number itself), 
from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) 
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

'''


import codewars_test as test
#from solution import divisors
#def divisors(integer):
def divisors(n):
    #pas
    ans=[ x for x in range(2,n) if n % x == 0 ]
    return ans if len(ans)>0 else f'{n} is prime'


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(15), [3,5])
        test.assert_equals(divisors(253), [11,23])
        test.assert_equals(divisors(24), [2,3,4,6,8,12])
        test.assert_equals(divisors(25), [5])
        test.assert_equals(divisors(13), "13 is prime")
        test.assert_equals(divisors(3), "3 is prime")
        test.assert_equals(divisors(29), "29 is prime")
