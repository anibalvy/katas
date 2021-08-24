def zero(x=False):  return eval(f'0{x}') if x else '0'#your code here 
def one(x=False):   return eval(f'1{x}') if x else '1'
def two(x=False):   return eval(f'2{x}') if x else '2'
def three(x=False): return eval(f'3{x}') if x else '3'
def four(x=False):  return eval(f'4{x}') if x else '4'
def five(x=False):  return eval(f'5{x}') if x else '5'
def six(x=False):   return eval(f'6{x}') if x else '6'
def seven(x=False): return eval(f'7{x}') if x else '7'
def eight(x=False): return eval(f'8{x}') if x else '8'
def nine(x=False):  return eval(f'9{x}') if x else '9'

def plus(x): return f'+{x}'
def minus(x): return f'-{x}'
def times(x): return f'*{x}'
def divided_by(x): return f'//{x}'


test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
