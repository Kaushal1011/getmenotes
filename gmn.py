import argparse
import sys

from gmnhash import gmnhash


class gmn:
    def __init__(self,filename:str):
        self.filename=filename
        self.gmnhash=gmnhash(self.filename)
        self.gmnhash.makehashtable()
        self.hashtable=self.gmnhash.hashtable
        self.Title="GMN _Notes"
        self.Author="Kaushal"
        self.markdownname=self.Title+".md"


    def makemarkdown(self):
        self.outfile=open(self.markdownname,"w+")
        self.outfile.write("# "+self.Title+"\n")
        self.outfile.write("Author: "+ self.Author+'\n')
        keys=self.hashtable.keys()
        for i in keys:
            self.outfile.write("## "+ i + '\n')
            points=self.hashtable[i]
            for j in points:
                self.outfile.write("- " + j[0] + " \n")
                if j[1]!='':
                    self.outfile.write("```python\n"+j[1]+"\n```\n")

        self.outfile.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='GMN-getmenotes "A Documentation tool"'
    )
    parser.add_argument('inputfile', help='source file')

    args = parser.parse_args()
    print(args.inputfile)
    GMN=gmn(args.inputfile)
    GMN.makemarkdown()
