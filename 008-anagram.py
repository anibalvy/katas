def anagrams(word, words):
    #your code here
    letters=[ x for x in word]
    res=[]
    for w in words:
        if len(w) == len(letters):
            wx=[ x for x in w]
            [ wx.pop(wx.index(x)) for x in letters if x in wx]
            h=res.append(w) if len(wx)==0 else 0
    return res



test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])


# check also with a word < to the looked for...
