#Mae Pereyra
import re

def CutLineOneToken(str1):
    outList = []
    Keywords = re.match(r'int\s|if\s|else\s|float\s',str1)
    if (Keywords != None):
        outList.append("<key ,"+ Keywords.group()+ " >")
        str1 = str1.replace(Keywords.group(0), "")
        print("<key,", Keywords.group(), " >")

    Identifiers = re.match(r'[A-Za-z]+[0-9]+\s',str1)
    if (Identifiers != None):
        outList.append("<id ,"+ Identifiers.group()+ " >")
        str1 = str1.replace(Identifiers.group(0), "")
        print("<id, ", Identifiers.group(), " >")

    Operators = re.match(r'=|\+|>|\*',str1)
    if (Operators != None):
        outList.append("<op ,"+ Operators.group()+ " >")
        str1 = str1.replace(Operators.group(0), "")
        print("<op, ", Operators.group(), " >")

    int_Literal = re.match(r'\s+\d', str1)
    if (int_Literal != None):
        outList.append("<lit ,"+ int_Literal.group()+ " >")
        str1 = str1.replace(int_Literal.group(0), "")
        print("<lit, ", int_Literal.group(), " >")

    float_Literal = re.match(r'[0-9+]+\.+[0-9]',str1)
    if (float_Literal != None):
        outList.append("<lit ,"+ float_Literal.group()+ " >")
        str1 = str1.replace(float_Literal.group(0), "")
        print("<lit, ", float_Literal.group(), " >")

    string_Literal = re.match(r'\s[A-Za-z]+',str1)
    if (string_Literal != None):
        outList.append("<lit ,"+ string_Literal.group()+ " >")
        str1 = str1.replace(string_Literal.group(0), "")
        print("<lit ", string_Literal.group(), " >")

    Separators = re.match(r'\(|\)|:|"|;', str1)
    if (Separators != None):
        outList.append("<sep ,"+ Separators()+ " >")
        str1 = str1.replace(Separators.group(0), "")
        print("<sep, ", Separators.group(), " >")
        
    print(outList)

if __name__ == '__main__':
    str1 = "int A1 = 5"
    CutLineOneToken(str1)
    str2 = "float BBB2 = 1034.2"
    CutLineOneToken(str2)
    str3 = "float cresult = A1 + BBB2 * BBB2"
    CutLineOneToken(str3)
    str4 = "p1 = tinypie:"
    CutLineOneToken(str4)
    #int_Lit and float_Lit are kind of working but its just mixing with both sometimes
    #Didnt have the time to put it in a loop so thing like "tinypie" not working well. 
