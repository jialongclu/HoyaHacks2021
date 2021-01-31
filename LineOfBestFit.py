import numpy as np

class LineOfBestFit():
    m = None
    b = None

    def getLineOfBestFit(self, stockPrices):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array(stockPrices)
        self.m, self.b = np.polyfit(x, y, 1)
    
    def getSlope(self):
        return self.m

# x = LineOfBestFit()
# y = x.getLineOfBestFit([1,2,3,4,5])
# print(x.getM())


