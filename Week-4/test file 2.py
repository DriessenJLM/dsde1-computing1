def concatenate_sentences(sentence1, sentence2):
    first = sentence1[0]
    second = sentence1.capitalize()
    if second == first:
        return "yes"
print(concatenate_sentences("ello?","Goodbye."))