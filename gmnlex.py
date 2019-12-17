class gmnlexer:
    def __init__(self,filename:str):
            self.filename=filename
            self.file=open(self.filename,'r')

    def getline(self):
        line = self.file.readline()
        if line:
            return line        

    def getnexttoken(self):
        opentag=False
        closetag=False
        nextline=False
        codefound=False
        startlogging=False
        commentfound=False
        text=[]
        code=[]
        topic=[]
        while True:
            line=self.getline()
            for i in range(len(line)):
                if(line[i]==" " and startlogging==False):
                    continue
                elif (line[i]=="#" and startlogging==False):
                    commentfound=True
                elif commentfound==True and line[i:i+4]=="<gm>":
                    startlogging=startlogging=True
                elif startlogging==True and codefound==False:
                    text.append(line(i))
                else:
                    break
            nextline=True    
                    

                
            

        
        
            



if __name__=='__main__':
    GMN=gmnlexer("example.py")
    GMN.maketokenarray()