Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.






# primera solucion (no sabia que se podia sumar)
def find_it(seq):
    count=0
    prev=-999999
    seq.sort()
    for i in seq:
        if i == prev:
            count+=1
        else:
            if count%2 != 0:
                return prev
            prev=i
            count=1
    return prev if count%2 != 0 else 0

# segunda
def find_it(seq):
    return [x for x in seq if seq.count(x)%2 !=0 ][0]
# Best








test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
