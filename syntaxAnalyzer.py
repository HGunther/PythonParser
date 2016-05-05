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
	if lineString[0] == "I" and lineString[1] == "=":
		print str(tabs * "\t") + str(lineArray[0]) + " = <expr>" + " # <assign_statement>"
		processLine(lineString[2:], lineArray[2:], tabs + 1)
	elif lineString[0] == "K" and lineArray[0] == "return":
		print str(tabs * "\t") + str(lineArray[0]) + " => <expr>" + " # <return_statement>"
		processLine(lineString[1:], lineArray[1:], tabs + 1)
	elif lineString[0] == "K" and lineArray[0] == "if":
		if lineArray[-1] == ":":
			print str(tabs * "\t") + str(lineArray[0])
			processLine(lineString[1:-1], lineArray[1:-1], tabs + 1)
		else:
			print str(tabs * "\t") + " Error, not colon found at end of if_statement \':\'"
			print lineArray
	elif lineString[0] == "K" and lineArray[0] == "print":
		print str(tabs * "\t") + " <print_statement>"
		processLine(lineString[1:], lineArray[1:], tabs + 1)

	# Function call
	# elif lineString[0] == "I" and lineString[1] == "(":
	#


	else:
		# Expression is not supported
		print str(tabs * "\t") + str(lineArray) + " # Expression type is not supported"


		# sys.stdout.write('.')



def splitOnParenthesis(string):
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
	outer = string[: openPos + 1] + string[closePos: closePos + 1]
	inner = string[openPos + 1:closePos]
	remainder = string[closePos + 1:]
	return (outer, inner, remainder)


def getExpression():
	pass


def getParamList():
	pass


run()
