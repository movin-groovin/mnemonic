#!/usr/bin/python
#-*- encoding:utf-8 -*-

"""
Модуль для выведения слов из фала в случайном порядке,
разбитыми на группы с определенным количеством групп 
Example: ./words.py vorcub.txt 10 5. Т.е. вывести из файла
vorcub.txt 5 групп по 10 слов в каждом. Слова в файле словаря должны быть
по 1 на строку и быть первыми и единственными  строке, т.е. никаких 
пробелов и табуляций.
"""

import sys, random



len_args = 3


def checkArgs ():
	if len (sys.argv) < len_args: return False
	return True


def printStrings (data):
	for strr in data:
		print "  ",strr
	print "\n"
	return

	
def processInput (fileName, blckSize, blckNum):
	"""
	fileName - The name of a vocubalory file
	blckSize - Number of words in one block
	blckNum - Number of blocks
	"""
	data = []
	num = 0; i = 0; j = 0;
	
	for line in open (fileName):
		if line[len (line) - 2] == "\r": line = line[0 : (len (line) - 2)]
		elif line[len (line) - 1] == "\n": line = line[0 : (len (line) - 1)]
		if len (line) == 0: continue
		data.append (line)
	
	if len (data) < blckSize:
		print "Too few words in the file\n"
		return
	
	num = len (data) / blckSize
	random.seed ()
	random.shuffle (data)
	while i < blckNum:
		printStrings (data[j*blckSize : (j+1)*blckSize])
		i += 1
		j += 1
		if j == num:
			j = 0
			random.shuffle (data)
	
	return


def main ():
	try:
		if not checkArgs ():
			print "Enter the arguments: {0} file_name size_of_block" \
			" number_of_blocks".format (sys.argv[0])
			return 1
			
		processInput (sys.argv[1], int (sys.argv[2]), int (sys.argv[3]))
	except BaseException as Exc:
		print "Has caught an exception:"
		print "    ", Exc
	
	
	return 0



if __name__ == "__main__":
	main ()
#else:
	# importing like module





"""
>>> def drop_each(string, num):
...     return ''.join(string[i+1:i+num] for i in range(0, len(string), num))
... 
>>> drop_each("Python", 3)
'yton'
>>> drop_each("lexis", 3) # Тестируем на другой строке
'exs'
>>> drop_each("Python", 4) # Теперь удаляем символы с индексом, кратным 4
'ythn'
>>> 
"""









