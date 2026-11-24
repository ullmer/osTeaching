from playwright.sync_api import sync_playwright
from tkinter import *

class playwrightTkMgr:
  mgr, p, page, browser  = [None] * 4 # or None, None, None, None :-)
  executable_path        = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  defaultWeb             = "https://www.clemson.edu"
  autoLaunch             = True
  cbMsg                  = None

  def __init__(self): 
    if self.autoLaunch: self.launchPlaywright()

  def launchPlaywright(self):
    self.mgr = sync_playwright() 
    self.p   = self.mgr.start()
    self.browser = self.p.chromium.launch(headless=False, executable_path = self.executable_path)
    self.page    = self.browser.new_page()
    self.page.goto(self.defaultWeb)

  def simpleCb(self):
    print("playwrightTkMgr:simpleCb called")
    cbm = self.cbMsg
    if cbm is not None: self.page.evaluate(cbm)

#### main ####

pwtm = playwrightTkMgr()
cb   = pwtm.simpleCb
pwtm.cbMsg = "window.scrollTo({top: 1000, behavior: 'smooth'})"

root = Tk()                                                
b    = Button(root, text="Hello, world!", command=cb) 
b.pack()                                                   
root.mainloop()                                            

### end ###
