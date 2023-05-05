import tkinter as tk
from gingerit.gingerit import GingerIt

def correct_text(event):
    input_text = input_textbox.get("1.0", tk.END).strip()
    parser = GingerIt()
    corrected_text = parser.parse(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert("1.0", corrected_text['result'])

root = tk.Tk()
root.title("Grammar and Spelling Checker")
root.geometry("500x300")

# Input text box
input_textbox = tk.Text(root, wrap=tk.WORD, width=50, height=5)
input_textbox.pack(pady=10)
input_textbox.bind("<Return>", correct_text)

# Button to correct text
correct_button = tk.Button(root, text="Correct Text", command=lambda: correct_text(None))
correct_button.pack(pady=5)

# Output text box
output_textbox = tk.Text(root, wrap=tk.WORD, width=50, height=5)
output_textbox.pack(pady=10)

root.mainloop()
