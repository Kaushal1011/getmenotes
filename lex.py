class gmnlexer:
    def __init__(self,filename:str):
            self.filename=filename
            self.file=open(self.filename,'r')

    def getline(self):
        line = self.file.readline()
        if line:
            return line        

    def maketokenarray(self):
        pass


if __name__=='__main__':
    GMN=gmnlexer("example.py")
    while True:
        a=GMN.getline()
        print(a)
        if a is None:
            break
            