#! /usr/bin/env python 3.1
import sys

# conversion mappings

_1to9dict = {'0': '', '1': 'one', '2': 'two'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty'}

def num2words(num_string):
	if num_string == '0':
		return 'zero'
	if len(num_string) > 2:
		return "Sorry can only handle 1 or two digit numbers"
	
	num_string = '0' + num_string
	tens, ones = num_string[-2], num_string[-1]
	
	if tens == '0':
		return _1to9dict[ones]
	elif tens == '1':
		return _10to19dict[ones]
	else:
		return _20to90dict[tens] + ' ' + _1to9dict[ones]

def main():
	print(num2words(sys.argv[1]))
	
main()