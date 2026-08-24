def printLine(char_count:int = 20,char:str = "-",doEnter:bool = True):
    for _ in range(char_count):
        print(char,end="")
    if doEnter:
        print(end="\n")