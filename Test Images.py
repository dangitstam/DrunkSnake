__author__ = 'dangitstam'
import random

sweg = [10, 32]

i = random.randrange(0, 2, 1)
megasweg = sweg[i]

test = range(0, 10)

for number in test:
    print i
    print ""
    print megasweg
    i = random.randrange(0, 2, 1)

print sweg[1]

x = range(0, 2)

print max(x)