def solution(n):
    # TODO convert int to roman string
     num=[x for x in str(n)] 
     num.reverse() 
     R=[['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']] 
     in_roman_rev=[ R[x[0]][int(x[1])] for x in enumerate(num)] 
     in_roman_rev.reverse() 
     return ''.join(in_roman_rev) 


test.assert_equals(solution(1),'I', "solution(1),'I'")
test.assert_equals(solution(4),'IV', "solution(4),'IV'")
test.assert_equals(solution(6),'VI', "solution(6),'VI'")
test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
test.assert_equals(solution(1000), 'M', 'solution(1000), M')
test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
