# import the necessary modules
import time
from tkinter import Tk, Label, Text, Button, StringVar, messagebox

class TypingSpeedTest:
    def __init__(self):
        """
        Initializes GUI elements and other necessary variables
        """
        self.root = Tk()
        self.root.title('Typing Speed Test')

        self.start_time = None
        self.initial_text = None
        
        Label(self.root, text='Enter the initial text:', font=('Helvetica',16)).pack()

        self.initial_text_widget = Text(self.root, height=5, width=60, font=('Helvetica',16))
        self.initial_text_widget.pack()
        Button(self.root, text='Set Text', command=self.set_initial_text, font=('Helvetica',16)).pack()

        Label(self.root, text='Type the initial text below:', font=('Helvetica',16)).pack()

        self.text_widget = Text(self.root, height=10, width=60, font=('Helvetica',16))
        self.text_widget.pack()
        self.text_widget.bind('<Return>', self.check_speed)
        self.text_widget.bind('<Key>', self.start_timer)

        Button(self.root, text='Reset', command=self.reset, font=('Helvetica',16)).pack()

        self.result_string = StringVar()
        Label(self.root, textvariable=self.result_string, font=('Helvetica',16)).pack()

    def set_initial_text(self):
        """
        Function to set the initial text from the Text widget
        """
        self.initial_text = self.initial_text_widget.get('1.0', 'end-1c')

    def start_timer(self, event):
        """
        Function to start the timer
        """
        if self.start_time is None:
            self.start_time = time.time()

    def reset(self):
        """
        Function to reset the GUI and variables to their initial state
        """
        self.start_time = None
        self.text_widget.delete("1.0", 'end')
        self.result_string.set('')

    def check_speed(self, event):
        """
        Function to calculate and display typing speed and accuracy
        """
        if self.initial_text and self.start_time is not None:
            end_time = time.time()
            duration = end_time - self.start_time
            transcribed_text = self.text_widget.get('1.0', 'end-1c')
            
            words = len(transcribed_text.split())
            speed = (words / duration) * 60

            mistakes = sum(1 for a, b in zip(self.initial_text, transcribed_text) if a != b)
            if len(self.initial_text) > len(transcribed_text):
                mistakes += len(self.initial_text) - len(transcribed_text)
            
            self.result_string.set(f'Your typing speed is {speed:.2f} words per minute with {mistakes} mistakes.')
        else:
            if not self.initial_text:
                messagebox.showerror("Typing Speed Test", "Please set the initial text.")
            else:
                messagebox.showerror("Typing Speed Test", "Please start typing to initiate the timer.")

    def run(self):
        """
        Starts the tkinter mainloop
        """
        self.root.mainloop()

if __name__ == "__main__":
    test = TypingSpeedTest()
    test.run()
