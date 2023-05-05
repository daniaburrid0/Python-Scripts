# Tkinter GUI
# pip install customtkinter
import tkinter 
import customtkinter as customtk
customtk.set_appearance_mode("System")
customtk.set_default_color_theme("blue")
root = customtk.CTk()
# set title of gui
root.title("Tkinter GUI")
# set geometry of gui
root.geometry("500x500")
# Use Buttons
btn = customtk.CTkButton(master=root, text="Click Me")
btn.place(x=100, y=100)
# Use Text Labels
lbl = customtk.CTkLabel(master=root, text="Hello World")
lbl.place(x=100, y=200)
# Use Input Boxes
entry = customtk.CTkEntry(master=root)
entry.place(x=100, y=300)
# Use Checkboxes
check = customtk.CTkCheckBox(master=root, text="Check Me")
check.place(x=100, y=400)
# Use Radio Buttons
radio = customtk.CTkRadioButton(master=root, text="Radio Me")
# Multi-line Text
text = customtk.CTkTextbox(master=root)
text.place(x=100, y=500)
# Scrollbar
scroll = customtk.CTkScrollbar(master=root)
scroll.place(x=100, y=600)
# Listbox
listbox = customtk.CTkTextbox(master=root)
listbox.place(x=100, y=700)
# Run app
root.mainloop()