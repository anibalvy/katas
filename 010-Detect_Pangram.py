import string

def is_pangram(s):
    symbols=[x for x in string.punctuation + string.digits + ' ']
    return True if len(list(dict.fromkeys([ x.lower() for x in s if x not in symbols])))==26 else False 
pangram = "The quick, brown fox jumps over the lazy dog!"
#test.assert_equals(is_pangram(pangram), True)
print(is_pangram(pangram))

