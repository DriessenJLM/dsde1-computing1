def palindrome_sentence(sentence):
    import copy
    import string
    rev = copy.copy(sentence)
    rev = rev.casefold()
    rev.replace(',','')
    rev.replace('.','')
    rev.replace('!','')
    rev.replace(' ','')
    rev.replace(';','')
    rev.replace(':','')
    words = copy.copy(rev)
    words =''.join(reversed(sentence))
    if words == rev:
        return True
    else:
        return False
print(palindrome_sentence("Mr. Owl ate my metal worm"))