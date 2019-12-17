class gmntoken:
    """GMN Token Class that contains data"""

    def __init__(self, text: str, code: str, topic: str):
        """Constructor"""
        self.text = text
        self.code = code
        self.topic = topic
