'''
# PythonParser
Project for CS4700 Programming Languages

Students:
Hans Gunther A01077132
Mikaila Young A01741449
Francisco Arrieta A01245365
'''


keywords = {"False": "KEYWORD", "class": "KEYWORD", "finally": "KEYWORD",
"is": "KEYWORD", "return": "KEYWORD", "None": "KEYWORD", "continue": "KEYWORD",
"for": "KEYWORD", "lambda": "KEYWORD", "try": "KEYWORD", "True": "KEYWORD",
"def": "KEYWORD", "from": "KEYWORD", "nonlocal": "KEYWORD", "while": "KEYWORD",
"and": "KEYWORD", "del": "KEYWORD", "global": "KEYWORD", "not": "KEYWORD",
"with": "KEYWORD", "as": "KEYWORD", "elif": "KEYWORD", "if": "KEYWORD",
"or": "KEYWORD", "yield": "KEYWORD", "assert": "KEYWORD", "else": "KEYWORD",
"import": "KEYWORD", "pass": "KEYWORD", "break": "KEYWORD", "except": "KEYWORD",
"in": "KEYWORD", "raise": "KEYWORD", "print": "KEYWORD",

"+": "OPERATOR", "-": "OPERATOR", "*": "OPERATOR",  "**": "OPERATOR", "/": "OPERATOR",
"//": "OPERATOR", "%": "OPERATOR", "@": "OPERATOR", "<<": "OPERATOR", ">>": "OPERATOR", 
"&": "OPERATOR", "|": "OPERATOR", "^": "OPERATOR", "~": "OPERATOR", "<": "OPERATOR", 
">": "OPERATOR", "<=": "OPERATOR", ">=": "OPERATOR", "==": "OPERATOR", "!=": "OPERATOR", 

"(": "DELIMITER", ")": "DELIMITER", "[": "DELIMITER", "]": "DELIMITER",
"{": "DELIMITER", "}": "DELIMITER", ",": "DELIMITER", ":": "DELIMITER",
".": "DELIMITER", ";": "DELIMITER", "@": "DELIMITER", "=": "DELIMITER",
"->": "DELIMITER", "+=": "DELIMITER", "-=": "DELIMITER", "*=": "DELIMITER",
"/=": "DELIMITER", "//=": "DELIMITER", "%=": "DELIMITER", "@=": "DELIMITER",
"&=": "DELIMITER", "|=": "DELIMITER", "^=": "DELIMITER", ">>=": "DELIMITER",
"<<=": "DELIMITER", "**=": "DELIMITER",

"$": "ERROR",
"?": "ERROR",
"`": "ERROR",
}


def run():
    inFile = open("input.py", 'r')
    for line in inFile:
        remainingLine = line
        while len(remainingLine) > 0:
            if remainingLine[0].isspace():
                remainingLine = remainingLine[1:]
            elif remainingLine[0] == "#":
                remainingLine = ""
            elif remainingLine[0].isalpha():
                remainingLine = readWord(remainingLine)
            elif remainingLine[0].isdigit():
                remainingLine = readNumber(remainingLine)
            elif remainingLine[0] == '"' or remainingLine[0] == "'":
                remainingLine = readStringLiteral(remainingLine)
            else: # is punctuation
                remainingLine = readPunctuation(remainingLine)
    print "(ENDMARKER)"
    inFile.close()


def readWord(string):
    #if word is not keyword, it must be an ID
    word = ""
    while (string[0].isalnum() or string[0] == "_") and len(string) > 0:
        word += string[0]
        string = string[1:]
    if keywords.has_key(word):
        print "(KEYWORD " + str(word) + ")"
    else:
        print "(ID " + str(word) + ")"
    return string


def readNumber(string):
    #Stop at first period if there are no numbers after it
    #never accept more than 1 period
    number = ""
    while len(string) > 0:
        if string[0].isdigit():
            number += string[0]
        elif string[0] == "j":
            number += string[0]
        elif string[0] == "." and "." not in number:
            number += string[0]
        elif string[0] == "." and number.count(".") >= 1:
            print "(ERROR UNEXPECTED DECIMAL POINT)"
            return ""
        else:
            break
        string = string[1:]

    print "(LIT " + number + ")"
    return string


def readStringLiteral(string):
    #Check for """ and '''
    #print error if no closing quotes found on same line
    #should print error if no closing """ or ''' in document
    phrase = ""
    endPos = string.find(string[0], 1)
    if endPos == -1:
        print "(ERROR No end quotation mark at the end of string literal)"
        return ""
    else:        
        phrase = string[: endPos + 1]
        string = string[endPos + 1:]
        print "(LIT " + str(phrase) + ")"
    return string
        
    
def readPunctuation(string):
    # if this is not an accepted punctuation, it should be an error
    if keywords.has_key(string[0]) and (keywords[string[0]] != "ERROR"):
        print "(PUNCT " + " " + string[0] + ")"
    else: 
        print "(ERROR: '" + string[0] + "' is a punctuation not used in Python)" 
    return string[1:]


if __name__ == "__main__":
    run()
