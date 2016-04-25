

def run():
    #read from text file
    # start loop
        #read in tab level
        #if first symbol is id then...
        #if first symbol is punctuation...
    inFile = open("out.txt", 'r')
    for line in inFile:
        _type = line.split()[0]
        if _type == "(ENDMARKER)":
            pass
        elif _type == "(PUNCT":
            pass
        elif _type == "(KEYWORD":
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