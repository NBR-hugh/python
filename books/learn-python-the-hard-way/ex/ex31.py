print "You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?"

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity =="2":
        print "Your body suevives powered by a mind of jello. Good job!"
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "There is cave where many books,golds and medicines,what do you want?"
    print "1. Books."
    print "2. golds."
    print "3. medicines."

    pick = raw_input(">")

    if pick == "1":
        print "Good! God bless you!"
    elif pick == "2":
        print "Good! you are a mammonist!"
    elif pick == "3":
        print "Good! Those will save your life!"


else:
    print "You stumble around and fall on a knife and die. Good job!"
