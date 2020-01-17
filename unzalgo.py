#!/usr/local/bin/python3
import sys

output = ""

for char in sys.stdin.read():
	if not 0x0300 <= ord(char) <= 0x036F:
		output += char

print(output)
