def rgb(r, g, b):
    to_hex=lambda x: f'{min(255, max(x,0)):X}' if len(f'{min(255, max(x,0)):X}')>1 else f'0{min(255, max(x,0)):X}'
    return f'{to_hex(r)}{to_hex(g)}{to_hex(b)}'


test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")


# round to numbers
round = lambda x: min(255, max(x, 0))


# from others, this is nice:
def rgb(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
