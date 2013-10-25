#coding UTF-8
import math
import sys
import random

#試し割り関数
def isPrime(num):
	tmp = 3
	
	if num < 2:
		return 0
	if num == 2:
		return 1
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
			
#ミラー･ラビンテスト
def isPrime2(num,k=50):

	if num < 2:
		return 0
	if num == 2:
		return 1
	if num % 2 == 0:
		return 0

	d = (num-1)>>1
	while d % 2 == 0:
		d >>= 1
	
	for i in xrange(k):
		a = random.randint(1,num-1)
		t = d
		y = pow(a,t,num)
		while not t == num-1 and not y == 1 and not y == num-1: 
			y = pow(y,2,num)
			t <<= 1
		if not y == num-1 and t % 2 == 0:
			return 0
	return 1

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

for var in xrange(0,len(strPi)):
	PiList.append(int(strPi[var]))

while 1:
	obj = 0
	for var in xrange(0,digits):
		obj = obj * 10 + PiList[position+var]
	print "Trying "+str(obj)
	if isPrime2(obj) == 1:
		print obj
		break
	else:
		position = position + 1
		if position + 10 > len(strPi):
			print "Not Found"
			break
