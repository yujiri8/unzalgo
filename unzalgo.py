#!/usr/local/bin/python3
import sys

contents = sys.stdin.read()

new_contents = ""

for char in contents:
	if ord(char) <= 127:
		new_contents += char

print(new_contents)
