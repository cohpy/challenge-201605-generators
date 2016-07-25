import re
import random
import sys
import time

startwords = {}
dictionary = {}

def teach(sentence):
    '''
    Teaches sentences to the markov chain. Use only
    single sentences at a time.
    '''

    reg = re.compile('[a-zA-Z\'\\-]+')
    words = reg.findall(sentence)
    if len(words) < 2: return
    if words[0] in startwords:
        startwords[words[0]] += 1
    else:
        startwords[words[0]] = 1
    for x in range(len(words)-1):
        if words[x] in dictionary:
            if words[x+1] in dictionary[words[x]]:
                dictionary[words[x]][words[x+1]] += 1
            else:
                dictionary[words[x]][words[x+1]] = 1
        else:
            dictionary[words[x]] = {}
            dictionary[words[x]][words[x+1]] = 1
    if words[x] in dictionary:
        if '.' in dictionary[words[x]]:
            dictionary[words[x]]['.'] += 1
        else:
            dictionary[words[x]]['.'] = 1
    else:
        dictionary[words[x]] = {}
        dictionary[words[x]]['.'] = 1

def readblock(block):
    '''
    Reads a block of text (such as a book) and extracts
    the sentences to teach one at a time.
    '''

    reg = re.compile('\\s+[A-Za-z,;\'"\\s]+[.?!]')
    sentences = reg.findall(block)
    for x in sentences:
        teach(x)

def speak():
    '''
    Generator to produce random sentences
    '''

    start = True
    word = None
    while True:
        if start:
            word = pickword(startwords)
            start = False
        else:
            try:
                word = pickword(dictionary[word])
            except:
                word = '.'
            if word == '.':
                start = True
        yield word

def pickword(selection):
    '''
    Picks a random word from a dictionary (as in, a selection of words, not
    the "dictionary" variable)
    '''

    number = random.randint(0, sum(selection.values()))
    for x in selection.keys():
        number -= selection[x]
        if number <= 0:
            return x

if __name__ == '__main__':
    with open('pg83.txt', 'r') as f:
        readblock(f.read())

    speaker = speak()
    while True:
        word = speaker.next()
        if word == '.':
            sys.stdout.write('.')
        else:
            sys.stdout.write(' ' + word)
        time.sleep(0.3)
