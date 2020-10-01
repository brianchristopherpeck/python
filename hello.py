#!/usr/bin/python -tt
import sys

def DoesNotExist(name):
	print(name, "does not exist")

def Hello(name):
	if name == "Alice" or name == "Nick":
		# Concatenting Strings
		name = name + "!!!!"
		print("Hello", name)
	else:
		DoesNotExist(name)
	

def main():
	Hello(sys.argv[1])

if __name__ == '__main__':
	main()
		
