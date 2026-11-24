from playwright.sync_api import sync_playwright
from tkinter import *

mgr = sync_playwright() 
p   = mgr.start()
browser = p.chromium.launch(
  headless=False,
  executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
page = browser.new_page()
page.goto("https://www.clemson.edu")

#input("Press Enter...")
#page.evaluate("window.scrollTo({top: 1000, behavior: 'smooth'})")
#input("Press Enter2...")

def helloCB():
  print("hello was pushed")

root = Tk()                                                # Create the root (base) window 
b    = Button(root, text="Hello, world!", command=helloCB) # Create a label with words
b.pack()                                                   # Put the label into the window
root.mainloop()                                            # Start the event loop


### end ###
