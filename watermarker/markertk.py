import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

def apply_watermark(image_path, watermark_text):
    image = Image.open(image_path)
    print(type(image))
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)

    w, h = image.size
    font_size = int(min(w, h) / 6)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Create a transparent overlay
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw text on the transparent overlay
    draw.text((0, 0), watermark_text, fill=(255, 255, 255, 255), font=font)

    # Get the bounding box of the non-transparent area
    bbox = overlay.getbbox()
    
    # Calculate the position to start drawing text with additional spacing
    position = (w - (bbox[2] - bbox[0]) - 100, h - (bbox[3] - bbox[1]) - 100)
    
    # Draw the text on the image at the calculated position
    draw = ImageDraw.Draw(watermark_image)
    draw.text(position, watermark_text, fill=(255, 255, 255, 127), font=font)
    
    return watermark_image


def open_file_dialog():
    global watermarked_image  # Declare as global to be accessible in other functions
    file_path = filedialog.askopenfilename(title='Select Image')
    if file_path:
        watermarked_image = apply_watermark(file_path, watermark_entry.get())
        display_watermarked_image(watermarked_image)

def display_watermarked_image(watermarked_image):
    tk_image = ImageTk.PhotoImage(watermarked_image.convert('RGB'))
    label = tk.Label(window, image=tk_image)
    label.image = tk_image
    label.pack()

def save_watermarked_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])
    if file_path:
        watermarked_image.save(file_path)

def main():
    global window  # Declare as global to be accessible in other functions
    global watermark_entry  # Declare as global to be accessible in other functions
    window = tk.Tk()
    window.title("Watermark Application")

    watermark_entry = tk.Entry(window, width=30)
    watermark_entry.pack(pady=10)
    watermark_entry.insert(0, "Enter Watermark Text Here")

    open_file_btn = tk.Button(window, text="Open Image", command=open_file_dialog)
    open_file_btn.pack(pady=10)

    save_image_btn = tk.Button(window, text="Save Image", command=save_watermarked_image)
    save_image_btn.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
