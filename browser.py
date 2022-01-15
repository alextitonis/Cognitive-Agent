from pyppeteer import launch

class browser:
    def __init__(self):
        print()
        
    def load(self):
        self.browser = launch({ 'headless': True })
        self.page = self.browser.newPage()
        
    def goTo(self, page: str):
        self.page.goto(page)
        
    def getImage(self, imagePath):
        self.page.screenshot({'path': imagePath})
        
    def close(self):
        self.browser.close()