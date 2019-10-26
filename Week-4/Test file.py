def concatenate_sentences(sentence1, sentence2):
    first = sentence1[0]
    second = sentence1.capitalize()
    if second[0] != first:
        raise ValueError
    if sentence1[-1] == "!" or sentence1[-1] == "?" or sentence1[-1] == "." :
        pass
    else:
        raise ValueError
    third = sentence2[0]
    fourth = sentence2.capitalize()
    if fourth[0] != third:
        raise ValueError
    if sentence2[-1] == "!" or sentence2[-1] == "?" or sentence2[-1] == "." :
        return sentence1 + sentence2
    else:
        raise ValueError
print(concatenate_sentences("Hello!", "Goodbye!"))