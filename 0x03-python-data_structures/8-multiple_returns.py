#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        tuple_length = (len(sentence), None)
    else:
        tuple_length = (len(sentence), sentence[0])
    return (tuple_length)
