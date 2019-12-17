from gmnlex import gmnlex


class gmnhash:
    """gmn hash class makes hashtable from tokens returned by lexer"""

    def __init__(self, filename: str):
        self.filename = filename
        self.hashtable = {}

    def makehashtable(self):
        """Function that initialises hashtable with values"""
        GMN = gmnlex(self.filename)
        token = GMN.getnexttoken()
        # Skips first metadata token currently
        while token:
            token = GMN.getnexttoken()
            if token is not None:
                if token.topic not in self.hashtable.keys():
                    self.hashtable[token.topic] = []
                self.hashtable[token.topic].append([token.text, token.code])


# check gmn hash
if __name__ == '__main__':
    GMN = gmnhash("example.py")
    GMN.makehashtable()
    print(GMN.hashtable)
