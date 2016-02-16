#!/usr/bin/python -tt
def censor(text, word):
    listy= text.split()
    listy = [w.replace(word, '*' * len(word)) for w in listy]
    s = ' '
    print s.join(listy)
    

censor('hey hey hey', 'hey')