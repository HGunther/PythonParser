

def run():
    inFile = open("out.txt", 'r')
    for line in inFile:
        _type = line.split()[0]
        sym = line.split()[1]
        sym = line.split('"')[1]
        if _type == "(ENDMARKER)":
            pass
        elif _type == "(PUNCT":
            pass
        elif _type == "(KEYWORD":
            if sym == "if":
                pass
            elif sym == "return":
                pass
            else:
                pass
            pass
        elif _type == "(ID":
            pass
        elif _type == "(LIT":
            pass
        else:
            pass
    inFile.close()
    
def getExpression():
    pass
    
def getParamList():
    pass