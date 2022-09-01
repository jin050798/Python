from .Calculator import *

class MoreCalculator(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result