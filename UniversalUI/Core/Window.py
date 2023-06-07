from .CoreGeometry import uSize

class uWindow:
    
    def __init__(self, title: str, size: uSize):
        self.title = title
        self.size = size

    def Report(self):
        print(self.title)
        print("width: ", self.size.width, " height: ", self.size.height)