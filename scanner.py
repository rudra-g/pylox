import sys

def runlox(*args):
    if args:
        if len(args)>1:
            print("Usage: jlox [script]")
        else:
            run_file(args[0])
    else:
        print("an interactive lox terminal")
        run_prompt()
        

def run_file(file):
    try:
        print(file)
        source = open(file,"r")
        print(source.read())
        run(source)
    except:
        print("error reading file")
    
def run_prompt():
    print("Prompt")
    while True:
        print("> ")
        line = input()
        if line and len(line)>0:
            run(line)
    
        
def run(source):
    scanner = Scanner(source)
    tokens = scanner.scanTokens()
    for token in tokens:
        print(token)
    pass
    
class Scanner():
    def __init__(self,source) -> None:
        self.source = source
    def scanTokens(self):
        return []
    
def report(line,location,message):
    print("[line ",line,"] Error",location,": ",message)
    
TokenType = ["LEFT_PAREN","RIGHT_PAREN","LEFT_BRACE","RIGHT_BRACE",
             "COMMA","DOT","MINUS","PLUS","SEMICOLON","SLASH",
             "STAR","BANG","BANG_EQUAL","GREATER","GREATER_EQUAL",
             "LESS","LESS_EQUAL","IDENTIIFIER","STRING","NUMBER",
             "AND","CLASS","ELSE","FALSE","FUN","FOR","IF","NIL",
             "OR","PRINT","RETURN","SUPER","THIS","TRUE","VAR","WHILE",
             "EOF"]

class Token():
    def __init__(self,type,lexeme,literal,line) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def to_string(self):
        information_string = self.type+" "+self.lexeme+" "+self.literal
        return information_string
    
    
runlox(1,2,3)
runlox(1)
runlox()