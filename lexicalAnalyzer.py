import sys
import re

keywords = {"False": "KEYWORD", "class": "KEYWORD", "finally": "KEYWORD",
"is": "KEYWORD", "return": "KEYWORD", "None": "KEYWORD", "continue": "KEYWORD",
"for": "KEYWORD", "lambda": "KEYWORD", "try": "KEYWORD", "True": "KEYWORD",
"def": "KEYWORD", "from": "KEYWORD", "nonlocal": "KEYWORD", "while": "KEYWORD",
"and": "KEYWORD", "del": "KEYWORD", "global": "KEYWORD", "not": "KEYWORD",
"with": "KEYWORD", "as": "KEYWORD", "elif": "KEYWORD", "if": "KEYWORD",
"or": "KEYWORD", "yield": "KEYWORD", "assert": "KEYWORD", "else": "KEYWORD",
"import": "KEYWORD", "pass": "KEYWORD", "break": "KEYWORD", "except": "KEYWORD",
"in": "KEYWORD", "raise": "KEYWORD",

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

"$": "ERROR: symbol not used in python",
"?": "ERROR: symbol not used in python",
"`": "ERROR: symbol not used in python",
}

    
def tokenize(string):
    string.strip()
    string.replace(" ", "")
    return re.compile("(!|@|#|%|&|\(|\)|\{|\}|\[|\]|\||\\|\.|\"|;|<|>|\/|_|\+|-|,|\$|\^|\*|\'|\?|=)").split(string)

if __name__ == "__main__":
    pass
    
def run():
    inFile = open("testInput.py", 'r')
    for line in inFile:
        remainingLine = line
        while len(remainingLine > 0):
            if remainingLine[0].isspace():
                remainingLine = remainingLine[1:]
            elif remainingLine[0] == "#":
                remainingLine = ""
            elif remainingLine[0].isalpha():
                readWord(remainingLine)
            elif remainingLine[0].isdigit():
                readNumber(remainingLine)
            elif remainingLine[0] == '"' or remainingLine[0] == "'":
                readStringLiteral(remainingLine, inFile)
            else: # is punctuation
                readPunctuation(remainingLine)
    print( "(ENDMARKER)" )
    inFile.close()
    
def readWord(string):
    #if word is not keyword, it must be an ID
    pass
    
def readNumber(string):
    #Stop at first period if there are no numbers after it
    #never accept more than 1 period
    pass
    
def readStringLiteral(string, inFile):
    #Check for """ and '''
    #print error if no closing quotes found on same line
    #should print error if no closing """ or ''' in document
    pass
    
def readPunctuation(string):
    # if this is not an accepted punctuation, it should be an error
    print"(PUNCT) " + str(string[0])
    string = string[1:]