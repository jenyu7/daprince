#Team jajajaja - Alessandro Cartegni & Jennifer Yu
#SoftDev2 pd7
#K18 - Reductio ad absurdum
#2018-04-30

from functools import reduce

fd = open('theprince.txt', 'r')
contents = fd.read().lower().strip('!''$''?''/''['']'',''.''&''-')
fd.close()

text = contents.split()


#returns number of times "prince" appears

#test case
story = ["hello", "my", "prince"]
print(reduce((lambda x,y:x+y),[1 for x in story if x == "prince"]))

def freqW(word):
    print(reduce((lambda x,y:x+y),[1 for x in text if x == word]))


#returns number of times a group of words appears

def freqG(phrase):
    n = len(phrase.split())
    print reduce((lambda x, y: x + y), [1 if phrase == reduce((lambda x, y: x + " " + y), text[text.index(x):text.index(x)+n]) else 0 for x in text ])


#returns most common word

def freq():
    print(reduce((lambda x,y:x+y), [x for x in max(x for x in text)]))


#function test cases
freqW("prince")
freqG("hello there ia masdfasdf ")
freq()
