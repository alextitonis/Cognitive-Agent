import pyscreenshot as ImageGrab

def takeScreenshot():
    return ImageGrab.grab()

im = takeScreenshot()
im.show();