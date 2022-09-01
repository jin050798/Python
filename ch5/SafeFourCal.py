from .Calculator import *

class SafeFourCal(Calculator):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second