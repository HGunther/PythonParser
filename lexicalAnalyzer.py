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
    inFile = open("input.py", 'r') # opens file as read-only
    for line in inFile:
        tokens = tokenize(line)
        #for token in tokens:
            #pass
            
    print( "(ENDMARKER)" )
    inFile.close()
    
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
            elif remainingLine[0] == '"':
                readStringLiteral(remainingLine)
            else: # is punctuation
                print"(PUNCT) " + str(remainingLine[0])
                remainingLine = remainingLine[1:]
    print( "(ENDMARKER)" )
    inFile.close()
    
def readWord(string):
    pass
    
def readNumber(string):
    pass
    
def readStringLiteral(string):
    pass