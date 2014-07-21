#!/usr/bin/python
#-*- encoding:utf-8 -*-


"""
Выводит числа на консоль. Использование: ./digits.py grp_num grp_len
Формат вывода - десятичный, 1 параметр - кол-во групп, 2 параметр - кол-во
чисел в группе. Например: ./digits.py 10 2 - 10 груп по 2 цифры
"""


import sys, random



BaseDigit = 10
OutputLen = 90


def outputNumerics (grpNum, grpSize):
	i = 0
	strOut = ""
	
	if grpSize > OutputLen:
		print ("Too big length of a group")
		return
	
	random.seed ()
	while i < grpNum:
		i += 1
		tmpStr = str (random.randint (0, BaseDigit ** grpSize - 1))
		if len (tmpStr) < grpSize:
			tmpStr = tmpStr.rjust (grpSize, "0")
		strOut += tmpStr + " "
		if len (strOut) >= OutputLen:
			print "  ", strOut
			strOut = ""
	if len (strOut) > 0:
		print "  ", strOut
	
	return


def start ():
	try:
		if len (sys.argv) < 2:
			print ("Example of startup: ./digits.py 10 5. 10 \
				    groups with 5 numerics in each")
			return
		outputNumerics (int (sys.argv[1]), int (sys.argv[2]))
	except BaseException as Exc:
		print ("Have caught an exception: ",Exc)
	return
	

if __name__ == "__main__":
	start ()
#else:
#	like a module
