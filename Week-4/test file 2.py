def palindrome_sentence(sentence):
    import copy
    import string
    rev = copy.copy(sentence)
    rev = rev.casefold()
    s = rev
    s = s.replace(',','')
    s = s.replace('.','')
    s = s.replace('!','')
    s = s.replace(' ','')
    s = s.replace(';','')
    s = s.replace(':','')
    words = copy.copy(s)
    words =''.join(reversed(s))
    print(words)
    if words == s:
        return True
    else:
        return False
print(palindrome_sentence("Mr. Owl ate my metal worm"))