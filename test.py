import threading
import time
import tkinter as tk

def heavy_computation():
    # Simulating heavy computation
    for _ in range(10):
        print("Computing...")
        time.sleep(1)

def gui_thread():
    root = tk.Tk()
    label = tk.Label(root, text="GUI running in separate thread")
    label.pack()
    root.mainloop()

# Create and start the threads
computation_thread = threading.Thread(target=heavy_computation)
gui_thread = threading.Thread(target=gui_thread)

computation_thread.start()
gui_thread.start()
