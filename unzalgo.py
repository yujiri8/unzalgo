#!/usr/local/bin/python3
import sys

contents = sys.stdin.read()

new_contents = ""

for char in contents:
	if not 0x0300 <= ord(char) <= 0x036F:
		new_contents += char

print(new_contents)
