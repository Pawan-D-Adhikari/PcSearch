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
    search_items=[
    "latest Python 3.11 features",
    "top programming languages 2024",
    "best Python IDEs for beginners",
    "Python data visualization libraries",
    "how to use GitHub Copilot with Python",
    "Python vs JavaScript for web development",
    "examples of Python machine learning projects",
    "most popular Python frameworks for 2024",
    "tips for debugging Python code",
    "how to deploy Python apps to the cloud"
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