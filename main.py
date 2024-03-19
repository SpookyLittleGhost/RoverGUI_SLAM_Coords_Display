import threading

import gui_display
import input_listener

print("!-- MAIN PROGRAM STARTED --!")

gui_display.prepare_window_size()

gui_display_thread = threading.Thread(target=gui_display.start, args=())
input_listener_thread = threading.Thread(target=input_listener.start, args=[gui_display])

input_listener_thread.start()
gui_display_thread.start()

input_listener_thread.join()
gui_display_thread.join()

print("!--- MAIN PROGRAM TERMINATED ---!")
