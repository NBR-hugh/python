# encoding:utf-8

# ex41 学习面对对象术语

import random
from urlib import  urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
  "make a class named %%% that is -a %%%.",
  "class %%%(objiect):\n\tdef__init__(self,***)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
  "*** = %%%()":
    " Set *** to an instance of class %%%.",
  "***.***(@@@)":
    "From *** get the *** fucntion,and call it with parameters self,@@@.",
  "***.***='***'":
    "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys,argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True


# load up the words form the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet,phrase):
    class_names = [w.capitalize() for w in 
                  random.sample(WORDS,snippet.count('%%%'))]
    other_names =  random.sample(WORDS,snippet.count("***"))
    result = sentence[:]

    # fake class name 
    for word in class_names:
        result = result.replace("%%%",word,1)

    # fake other names
    for word in other_names:
        result = result.replace("***",words,1)

    # fake parameter lists
    for word in param_names:
        result =result.replace("@@@",words,1)

    results.append(result)

return results


# keep going untiall they hit CTRL-D
try:
    while True:
        snippet = PHRASES.keys()
        random.shuffle(snippet)

        for snippet in snippet:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)
        if PHRASES_FIRST:
            question,answer = answer,question

        print question

        raw_input("> ")
        print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
