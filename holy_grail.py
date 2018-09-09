"""This program is for storing all of your most dirty secrets"""
#Lines are taken according to the online transcript of the bridge
#scene from MP Holy Grail. Scipt used:
#URL: http://www.mit.edu/afs.new/sipb/user/ayshames/Python/BRIDGE.PYTHON

from time import sleep
from random import randint

dictionary = {
"Favorite Animal" : "Zebra",
"Top Secret Code" : "1234"
}

#prints the items from the dictionary onto the terminal.
def dictionary_fun(dict):
    for item in sorted(dictionary):
        print item + ": ", dict[item]
        sleep(0.75)

#prints lines
def lines():
    for i in range(0, 5):
        print "--------------------"
        sleep(0.5)

#shows welcome message and takes name input.
def welcome_sequence():
    print "Stop!"
    sleep(3)
    print "Who approacheth the Bridge of Death"
    sleep(1)
    print "Must answer me"
    sleep(1)
    print "These answers three"
    sleep(1)
    print "Ere the other side he see."
    sleep(2)

#function for Launcelot's questions
def launcelot():
    quest = raw_input("What...is your quest? ").lower()
    if quest == "to seek the holy grail":
        color = raw_input("What...is your favorite color? ").lower()
        if color == "blue":
            sleep(1)
            print "Right. Off you go."
            sleep(2)
            lines()
            dictionary_fun(dictionary)
        else:
            sleep(2)
            print "You may not cross the bridge."
    else:
        sleep(2)
        print "You may not cross the bridge."

#function for Robin's questions
def robin():
    quest = raw_input('What...is your quest? ').lower()
    if quest == 'to seek the holy grail':
        capital = raw_input('What...is the capital of Assyria? ')
            #Need to actually find the capital of Assyria lol
        if capital == "assur":
            sleep(1)
            print "Oh...you weren't suppose to know that"
            sleep(2)
            print "Oh well, Off you go."
            sleep(2)
            lines()
            dictionary_fun(dictionary)
        else:
            print "You may not cross the bridge."
    else:
        print "You may not cross the bridge."

#function for galahad's questions
def galahad():
    quest = raw_input('What...is your quest? ').lower()
    if quest == 'i seek the grail':
        color = raw_input('What...is your favorite color? ')
        if color == 'yellow':
            sleep(1)
            print "Right. Off you go."
            sleep(2)
            lines()
            dictionary_fun(dictionary)
        elif color == 'blue':
            print "You may not cross the bridge."
        else:
            print "You may not cross the bridge."
    else:
        print "You may not cross the bridge."

#function(my favorite) for Arthur's questions
def arthur():
    quest = raw_input('What...is your quest? ')
    if quest == 'to seek the holy grail':
        swallow = raw_input("What...is the air-speed velocity of an unladen swallow? ").lower()
        if swallow == "what do you mean? an african or european swallow?":
            sleep(1)
            print "What?"
            sleep(2)
            print "I don't know that! Auuuuuuuuuugh!"
            sleep(2)
            lines()
            dictionary_fun(dictionary)
        else:
            sleep(2)
            print "You may not cross the bridge."
    else:
        print "You may not cross the bridge."

#puts together and executes all functions
def main_sequence():
    welcome_sequence()
    name = raw_input("What...is your name? ").lower()
    if name == "my name is sir launcelot of camelot":
        launcelot()
    elif name == "sir robin of camelot":
        robin()
    elif name == "sir galahad of camelot":
        galahad()
    elif name == "it is arthur, king of the britons":
        arthur()
    else:
        print "You may not cross the bridge."

main_sequence()
