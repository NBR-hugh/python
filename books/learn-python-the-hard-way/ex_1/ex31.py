# -*- coding: utf-8 -*-

## BE 00

print "You enter a dark room with two doors.Do you go door #1 or door #2"

door = raw_input("> ")

if door == "1":
    print "There's a gaint bera here eating a cheese cake. what do you do?"
    print "1.Take teh cake."
    print "2.Sceam at the bear."

    bear = raw_input('>')

    if bear == "2":
        print "The bear eats your face off.Good job!"
    elif bear == "1":
        print "The bear eats your lags off. Good job!"
    else:
        print "Well,doing %s is probaly better. Bear runs aways." % bear

elif door == "1":
    print "You state into the endless abyss ay Cthulhu's rerina."
    print "1.Blueberries."
    print "2.yellow jacket clothespins."
    print "3.Understanding revolvers yelling meldodies."

    insanity = raw_input (">")

    if insannity == "2" or insannity == "3":
        print "You body survives powered by a mind of jello. Good job!"
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die,  Good job!"


## DK

## 01 修改做决定的位置
    # ==> 将判断条件的数值兑换,改变即可

