import sys

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
			print str(tabs * "\t") + " <expr>"
			return

	print lineString
	# print lineArray

	# Assignments
	if lineString[0] == "I" and lineString[1] == "=":
		print str(tabs * "\t") + str(lineArray[0]) + " = <expr>" + " # <assign_statement>"
		processLine(lineString[2:], lineArray[2:], tabs + 1)

	# return statements
	elif lineString[0] == "K" and lineArray[0] == "return":
		print str(tabs * "\t") + str(lineArray[0]) + " => <expr>" + " # <return_statement>"
		processLine(lineString[1:], lineArray[1:], tabs + 1)

	# If statements
	elif lineString[0] == "K" and lineArray[0] == "if":
		if lineArray[-1] == ":":
			print str(tabs * "\t") + str(lineArray[0])
			processLine(lineString[1:-1], lineArray[1:-1], tabs + 1)
		else:
			print str(tabs * "\t") + " Error, not colon found at end of if_statement \':\'"
			print lineArray

	# Print statements
	elif lineString[0] == "K" and lineArray[0] == "print":
		print str(tabs * "\t") + " <print_statement>"
		processLine(lineString[1:], lineArray[1:], tabs + 1)

	# Function call
	elif lineString[0] == "I" and lineString[1] == "(":
		outerString, outerArray, innerString, innerArray, remainderString, remainderArray = splitOnParenthesis(lineString, lineArray)
		print str(tabs * "\t") + str(outerArray[0:2]) + " <expr> " + str(outerArray[2])
		processLine(innerString, innerArray, tabs + 1)
		processLine(remainderString, remainderArray, tabs)


	else:
		# Expression is not supported
		print str(tabs * "\t") + str(lineArray) + " # Expression type is not supported"


		# sys.stdout.write('.')




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


def getExpression():
	pass


def getParamList():
	pass


run()
