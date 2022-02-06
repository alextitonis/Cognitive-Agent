import asyncio
from pyppeteer import launch

class browser:
    async def load(self):
        self.browser = await launch()
        self.page = await self.browser.newPage()
        
    async def goTo(self, page: str):
        await self.page.goto(page)
        
    async def getImage(self, imagePath, fullPage=True):
        await self.page.screenshot({'path': imagePath, 'fullPage': fullPage})
        
    async def close(self):
        await self.browser.close()
        
    async def evaluate(self, func):
        return await self.page.evaluate('''() => { ''' + str(func) + '''}''');

async def example():       
    b = browser()
    await b.load()
    await b.goTo('https://www.google.com')
    await b.getImage('google.png')

def runExample():
    asyncio.get_event_loop().run_until_complete(example())