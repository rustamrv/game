import json

class WorkFile:

    def __init__(self, file):
        self.file = file 

    def read(self):
        file = open(self.file, mode="r")
        return json.load(file)


