
import UniversalUI
from UniversalUI.Core import Debug
from UniversalUI.Core import CoreGeometry
from UniversalUI.Core.CoreGeometry import uSize
from UniversalUI.Core import Window

UniversalUI.uuiInit()
Debug.UUIPrint("hello world")

mySize = uSize(200.0, 500.0)
myWindow = Window.uWindow(20 + 5, 600)
myWindow.Report()