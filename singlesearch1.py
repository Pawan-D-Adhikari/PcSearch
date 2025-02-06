import pyautogui as gui
import time
def main():
    first_search()
    other_search()
    
    
def first_search():
    gui.moveTo(1815,18,duration=0.2)
    gui.click()
    time.sleep(0.5)
    gui.moveTo(811,330,duration=1)
    time.sleep(0.5)
    gui.click()
    time.sleep(0.5)
    gui.write("Hello World",interval=0.2)
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(5)
    
    
def other_search():
    gui.PAUSE=2.5
    search_items = [
    "top political issues in 2025",
    "latest global economic trends",
    "impact of AI on politics",
    "most influential world leaders today",
    "rising political movements in 2025",
    "social media's role in modern politics",
    "climate change policies worldwide",
    "future of cryptocurrency regulations",
    "elections and political shifts in 2025",
    "geopolitical conflicts and resolutions"
    ]
    for i in search_items:
        gui.moveTo(710,126,duration=1.5)
        
        gui.click()
        gui.write(i,interval=0.2)
        gui.press("enter")
        gui.scroll(-2000)
        time.sleep(4)
        gui.scroll(2000)
        time.sleep(2)
    


main()