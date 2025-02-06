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
    "most popular sports in the world",
    "history of the Olympic Games",
    "top esports tournaments in 2025",
    "how virtual reality is changing gaming",
    "best sports video games of all time",
    "impact of AI in modern gaming",
    "evolution of football tactics",
    "psychology behind competitive gaming",
    "highest-paid athletes in 2025",
    "future of blockchain in gaming"
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