#coding UTF-8
import math
import sys

#試し割り関数
def isPrime(num):
	tmp = 3
	
	if num < 2:
		return 0
	if num % 2 == 0:
		return 0

	while 1:
		if num % tmp == 0:
			return 0
		tmp = tmp + 2
		if tmp > int(math.sqrt(num)):
			return 1

	for var in TmpList:
		if num % var == 0:
			return 0

#変数群
Pi = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
strPi = str(Pi)
PiList = []
position = 0
obj = 0

#コマンドライン引数解析
argvs = sys.argv
argc = len(argvs)

if not argc == 2:
	print "Argument is incorrect."
	exit()

if not argvs[1].isdigit():
	print "Argument is incorrect."
	exit()

digits = int(argvs[1])

for var in range(0,len(strPi)):
	PiList.append(int(strPi[var]))

while 1:
	obj = 0
	for var in range(0,digits):
		obj = obj * 10 + PiList[position+var]
	print "Trying "+str(obj)
	if isPrime(obj) == 1:
		print obj
		break
	else:
		position = position + 1
		if position + 10 > len(strPi):
			print "Not Found"
			break
