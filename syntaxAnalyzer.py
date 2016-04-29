

def run():
    inFile = open("out.txt", 'r')
    lineString = ""
    lineArray = []
    for line in inFile:
        if line == "(ENDMARKER)\n":
            #end of program
            #print output
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

    
def processLine(lineString, lineArray):
    print lineString
    
    
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
    outer = string[:openPos+1] + string[closePos:closePos+1]
    inner = string[openPos+1:closePos]
    remainder = string[closePos+1:]
    return (outer, inner, remainder)
    
    
def getExpression():
    pass
    
def getParamList():
    pass