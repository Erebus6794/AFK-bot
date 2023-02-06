import pyautogui as pag
import random
import time
import tkinter as tk

def start_afk():
    global running
    running = True
    curr_coords = pag.position()
    afk_counter = 0
    while running:
        root.update()
        if pag.position() == curr_coords:
            afk_counter += 1
        else:
            afk_counter = 0
            curr_coords = pag.position()
        if afk_counter > 5:
            x = random.randint(1, 1920)
            y = random.randint(1, 1080)
            pag.moveTo(x, y, 0.5)
            curr_coords = pag.position()
        print(f'AFK Counter: {afk_counter}')
        time.sleep(1)

def stop_afk():
    global running
    running = False
    print("Stopped")

root = tk.Tk()
root.geometry("200x50")
root.title("AFK Bot")

start_button = tk.Button(root, text="Start", command=start_afk)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_afk)
stop_button.pack()

root.mainloop()
