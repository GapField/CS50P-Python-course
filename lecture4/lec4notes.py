import random
from random import choice
'''
coin= random.choice(["heads","tails"]) #randomize between the item
print(coin)

coin = choice(["heads","tails"])

number = random.randint(1,10) #random number betwwen 1 and 10
print(number)

cards= ["jack","queen","king"]
random.shuffle(cards) #will not return a value, shufflle the items in the list only
for card in cards:
    print(card)

import statistics
print(statistics.mean([100,90]))

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
'''
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, "+ sys.argv[1])