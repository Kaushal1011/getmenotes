from gmnbase import gmntoken


class gmnlex:
    """lexer class of getmenotes: Makes tokens from reading code"""

    def __init__(self, filename: str):
        self.filename = filename
        self.file = open(self.filename, 'r')

    def getline(self) -> str:
        """Read one line from file"""
        line = self.file.readline()
        if line:
            return line

    def getnexttoken(self) -> gmntoken:
        """returns a token by reading the file"""
        opentag = False
        closetag = False
        commentfound = False
        topicflag = None
        skip = False
        text = []
        code = []
        topic = []
        skipper = 0

        # <gm>[Lexer] check for comment
        # check for start tag, check topic if not set global
        # check for code lines
        # </gm>
        while True:
            """token making logic follows gmn grammer"""
            line = self.getline()
            if line is not None:
                for i in range(len(line)):
                    # print(opentag,closetag,text,code,topic,line[i])
                    if skip == True and i <= skipper:
                        continue
                    else:
                        skip = False
                    if line[i] == "#" and commentfound == False:
                        commentfound = True
                    if commentfound == False and opentag == False:
                        continue
                    if commentfound == True and opentag == False and line[i:i+4] == "<gm>":
                        opentag = True
                        skip = True
                        skipper = i+4
                        continue
                    if opentag == True and topicflag is None:
                        if line[i] != ' ':
                            if line[i] == '[':
                                j = i+1
                                while line[j] != ']':
                                    topic.append(line[j])
                                    j += 1
                                skip = True
                                skipper = j
                                topicflag = True
                                continue
                            else:
                                topicflag = False
                                topic.append('global')
                                continue
                    if opentag == True and topicflag is not None:
                        if commentfound == True:
                            if(line[i:i+5] == "</gm>"):
                                closetag = True
                                break
                            if line[i] != '#':
                                text.append(line[i])
                        if commentfound == False:
                            code.append(line[i])
                        continue
                    if line[i:i+5] == "</gm>":
                        return None
                commentfound = False
                if closetag == True:
                    return gmntoken(''.join(text), ''.join(code), ''.join(topic))
            else:
                return None


# checks gmnlexer
if __name__ == '__main__':
    GMN = gmnlex("example.py")
    a = GMN.getnexttoken()
    while a:
        a = GMN.getnexttoken()
        if a is not None:
            print(''.join(a.topic))
