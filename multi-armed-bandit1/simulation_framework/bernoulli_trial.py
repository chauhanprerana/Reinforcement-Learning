import random


class BernoulliTrial():
    def __init__(self, p):
        self.p = p
        
    def draw(self):
        if random.random() > self.p:
            return 0
        else:
            return 1
