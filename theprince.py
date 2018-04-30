from functools import reduce

story = 

#adds with each occurence of "prince"
reduce((lambda x,y:x+y),[1 for x in story if x == "prince"])
