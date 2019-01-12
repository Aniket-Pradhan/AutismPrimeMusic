from getModPitch import myfunc 
from math import log


fileLines = []
with open("../Data/lmao.txt", 'r') as fileOut:
	for line in fileOut:
		fileLines.append(line.strip().split())

i=0
frq = 50

while i < len(fileLines):
	val = (fileLines[i][1])
	i += 30

	if float(val) == 0:
		continue
	octv = log(float(val)/60 ,2)
	myfunc(octv)
	

