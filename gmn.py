import argparse
import sys

from gmnhash import gmnhash


class gmn:
    """main gmn class that handles th working of the app"""

    def __init__(self, filename: str):
        self.filename = filename
        self.gmnhash = gmnhash(self.filename)
        self.gmnhash.makehashtable()
        self.hashtable = self.gmnhash.hashtable
        self.Title = "GMN _Notes"
        self.Author = "Kaushal"
        self.markdownname = self.Title+".md"

    def makemarkdown(self):
        """function that writes data to markdown using gmn hashtable"""

        self.outfile = open(self.markdownname, "w+")
        self.outfile.write("# "+self.Title+"\n")
        self.outfile.write("Author: " + self.Author+'\n')
        keys = self.hashtable.keys()
        for i in keys:
            self.outfile.write("## " + i + '\n')
            points = self.hashtable[i]
            for j in points:
                self.outfile.write("- " + j[0] + " \n")
                if j[1] != '':
                    self.outfile.write("```python\n"+j[1]+"\n```\n")

        self.outfile.close()


if __name__ == '__main__':
    """Main"""

    # argparser for gmn
    parser = argparse.ArgumentParser(
        description='GMN-getmenotes "A Documentation tool"'
    )
    parser.add_argument(
        'inputfile', help='source filename whose documentation is to be made')

    args = parser.parse_args()
    print(args.inputfile)
    GMN = gmn(args.inputfile)
    GMN.makemarkdown()
    print("Successful!")
