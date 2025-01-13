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
    gui.write("breaking Bad",interval=0.2)
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(5)
    
    
def other_search():
    gui.PAUSE=2.5
    search_items = [
    "best recipes for quick dinners",
    "how to train for a marathon",
    "latest space exploration news",
    "tips for managing personal finances",
    "top-rated video games 2024",
    "how to improve public speaking skills",
    "best cars for fuel efficiency",
    "current fashion trends for winter",
    "how to start a small business",
    "health benefits of drinking green tea"
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