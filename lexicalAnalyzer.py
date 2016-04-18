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

def isKeyword(string):
    return keywords.has_key(string)

if __name__ == "__main__":
    inFile = open("testInput.py", 'r') # opens file as read-only
    for line in inFile:
        pass
    inFile.close()