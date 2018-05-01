#Team jajajaja - Alessandro Cartegni & Jennifer Yu
#SoftDev2 pd7
#K18 - Reductio ad absurdum
#2018-04-30

from functools import reduce

fd = open('theprince.txt', 'r')
contents = fd.read()
fd.close()

text = contents.split()


#returns number of times "prince" appears

#test case
story = ["hello", "my", "prince"]
print(reduce((lambda x,y:x+y),[1 for x in story if x == "prince"]))

def freqW(word):
    print(reduce((lambda x,y:x+y),[1 for x in text if x == word]))


#returns number of times a group of words appears

def freqG(group):
    print(reduce((lambda x,y:x+y),[1 for x in text if x in group]))


#returns most common word

def freq():
    print(reduce((lambda x,y:x+y), [x for x in max(x for x in text)]))


#function test cases
freqW("prince")
freqG(["rule", "over"])
freq()
