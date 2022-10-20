class Man:
    def __init__(self, count):
        self.count = [1, 2, 3, 5, 6, 7, 8]

    def appendMe(self):
        if len(self.count) > 1:
            self.count.pop(0)
            print(self.count)
cmn = Man()

cmn.appendMe()