# -*- coding: utf-8 -*-

## BE 00

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    "Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    "Sorts the words then print_firstandlast one"
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    

if __name__ == '__main__':
    sentence = "All good things come to those who wait."
    words = break_words(sentence)
    sort_words = sort_words(words)
    print "sentence:",sentence
    print "words:",words
    print "break_words:",sort_words

    print_first_word(words)
    print_last_word(words)
    print_first_word(sort_words)
    print_last_word(sort_words)
    
    print sort_words

    print_first_and_last_sorted(sentence)
    print_first_and_last(sentence)
