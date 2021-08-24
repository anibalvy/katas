
# this fails some tests
def longest_consec(strarr, k):
    # your code
    # this didn't work in some cases, bad max return
    #return "" if len(strarr)==0 or k>len(strarr) or k<=0 else max([ (len(''.join([ strarr[x+i] for i in range(k)])),''.join([ strarr[x+i] for i in range(k)])) for x in range(len(strarr)-k+1)])[1]
    # using max(value, key=len) solved the issue
    return "" if len(strarr)==0 or k>len(strarr) or k<=0 else max([ ''.join(strarr[x:x+k]) for x in range(len(strarr)-k+1)],key=len)


# this works fine
def longest_consec(strarr, k):
    # your code
    print(strarr,k)
    if len(strarr)==0 or k>len(strarr) or k<=0:
        return ""
    else :
        #x=[ (len(''.join([ strarr[x+i] for i in range(k)])),''.join([ strarr[x+i] for i in range(k)])) for x in range(len(strarr)-k+1)]
        # improved below (I was using list comprehension when I just could use list[x:x+k]
        x=[ (len(''.join(strarr[x:x+k])),''.join([ strarr[x:x+k])) for x in range(len(strarr)-k+1)]
        return [i for i in x if i[0]==max(x)[0]][0][1]


 testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("longest_consec")
test.it("Basic tests")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
testing(longest_consec([], 3), "")
testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
