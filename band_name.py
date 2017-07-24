import random
import os


lines = ['']

try:
    text_file = open('words.txt', 'r')
    lines = list(text_file.read().split('\n'))

except:
    print('File not loaded.')
    lines = ['File not loaded']


def getName(words=0):
    title = ''
    s_used = 0
    if words == 0:
        words = random.choice([1,1,1,1,2,2,2,3,3,3,3,3,4])
    if random.choice([0,0,0,0,0,1]) or (words == 1 and random.choice([0,0,1])):
        title = "The "+title
    for word in range(0,words):
        title = title + random.choice(lines).strip().title() + ' '
        if (words - word) > 1:
            if random.choice([0,0,0,0,0,1]):
                title = title + 'of '
            elif random.choice([0,0,0,0,0,1]):
                title = title + 'the '
            elif random.choice([0,0,0,0,0,1]) and not s_used:
                title = title.strip() + "'s "
                s_used=1
    return title.strip().replace("'S","'s")

def getTweet(bn=""):
    if bn == "":
        bn = getBandName()
    return bn + "\n...Great name for a band!"