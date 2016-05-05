import sys

supported = []
unsupported = []

def run():
	inFile = open("out.txt", 'r')
	lineString = ""
	lineArray = []
	for line in inFile:
		if line == "(ENDMARKER)\n":
			# end of program
			# print output
			break
		_type = line.split()[0]
		sym = line.split()[1]
		sym = line.split('"')[1]
		if _type == "(PUNCT":
			if sym == "\\n":
				processLine(lineString, lineArray)
				lineString = ""
				lineArray = []
			else:
				if sym == "(":
					lineString += "("
				elif sym == ")":
					lineString += ")"
				elif sym == "=":
					lineString += "="
				else:
					lineString += "P"
				lineArray.append(sym)
		elif _type == "(KEYWORD":
			lineString += "K"
			lineArray.append(sym)
		elif _type == "(ID":
			lineString += "I"
			lineArray.append(sym)
		elif _type == "(LIT":
			lineString += "L"
			lineArray.append(sym)
		else:
			pass
	print "Reached the end!"
	inFile.close()


def processLine(lineString, lineArray, tabs=0):

	# Base case
	if len(lineArray) < 1:
		return
	if len(lineArray) == 1:
		if lineString[0] == "I" or lineString[0] == "L":
			s = str(tabs * "\t") + "<expr>: " + bracket_stripper(lineArray[0])
			print s
			supported.append(s)
			return
		else:
			print str(tabs * "\t") + "Error: statement type not supported statement"
			s = bracket_stripper(lineArray)
			print s
			unsupported.append(s)

	# Assignments
	if lineString[0] == "I" and lineString[1] == "=":
		s = str(tabs * "\t") + "<assign_statement>: " + str(lineArray[0]) + " = <expr>"
		processLine(lineString[2:], lineArray[2:], tabs + 1)
		print s
		supported.append(s)

	# return statements
	elif lineString[0] == "K" and lineArray[0] == "return":
		s = str(tabs * "\t") + "<return_statement>: return <expr>"
		processLine(lineString[1:], lineArray[1:], tabs + 1)
		print s
		supported.append(s)

	# If statements
	elif lineString[0] == "K" and lineArray[0] == "if":
		if lineArray[-1] == ":":
			s = str(tabs * "\t") + "<if_statement>: " +  str(lineArray[0])
			supported.append(s)
			processLine(lineString[1:-1], lineArray[1:-1], tabs + 1)
		else:
			print str(tabs * "\t") + "Error, no colon found at end of <if_statement>"
			s = bracket_stripper(lineArray)
			print s
			unsupported.append(s)

	# Print statements
	elif lineString[0] == "K" and lineArray[0] == "print":
		s = str(tabs * "\t") + "<print_statement>: print <expr>"
		print s
		supported.append(s)
		processLine(lineString[1:], lineArray[1:], tabs + 1)


	# Function call
	elif lineString[0] == "I" and lineString[1] == "(":
		outerString, outerArray, innerString, innerArray, remainderString, remainderArray = splitOnParenthesis(lineString, lineArray)
		s = str(tabs * "\t") + "<function_call>: " + bracket_stripper(outerArray[0:2]) + " <expr> " + bracket_stripper(outerArray[2])
		print s
		supported.append(s)
		processLine(innerString, innerArray, tabs + 1)
		processLine(remainderString, remainderArray, tabs)

	# Member function call
	elif lineString[0] == "I" and lineString[1] == "." and lineString[2] == "I" and lineString[3] == "(":
		outerString, outerArray, innerString, innerArray, remainderString, remainderArray = splitOnParenthesis(lineString, lineArray)
		s = str(tabs * "\t") + bracket_stripper(outerArray[0:2]) + " <expr> " + bracket_stripper(outerArray[2])
		print s
		supported.append(s)
		processLine(innerString, innerArray, tabs + 1)
		processLine(remainderString, remainderArray, tabs)
	else:
		# Expression is not supported
		print str(tabs * "\t") + "Error: statement type not supported statement"
		s = bracket_stripper(lineArray)
		print s
		unsupported.append(s)


def splitOnParenthesis(string, array):
	level = 0
	openPos = -1
	closePos = -1
	for i in range(len(string)):
		if string[i] == "(":
			level += 1
			if openPos == -1:
				openPos = i
		elif string[i] == ")":
			level -= 1
			if level == 0 and closePos == -1:
				closePos = i
	outerString = string[: openPos + 1] + string[closePos: closePos + 1]
	outerArray = array[: openPos + 1] + array[closePos: closePos + 1]
	innerString = string[openPos + 1:closePos]
	innerArray = array[openPos + 1:closePos]
	remainderString = string[closePos + 1:]
	remainderArray = array[closePos + 1:]
	return (outerString, outerArray, innerString, innerArray, remainderString, remainderArray)


def bracket_stripper(string):
	if type(string) == str:
		return string

	x = ""
	for i in string:
		x += i
		x += " "
	return x

def write_to_file():
	with open("parse_tree_output.txt", "w") as fin:
		fin.write("Count supported: " + str(len(supported)) + "\n")

		for i in range(len(supported)):
			fin.write(supported[i] + "\n")

		fin.write(str("\n" * 3))
		fin.write("Count not supported: " + str(len(unsupported)) + "\n")
		for i in range(len(unsupported)):
			fin.write(unsupported[i] + "\n")


	fin.close()

if __name__ == "__main__":
	run()
	write_to_file()
