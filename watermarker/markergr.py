from PIL import Image, ImageDraw, ImageFont
import gradio as gr
import logging

# Configure logging at the start of the script
logging.basicConfig(filename='watermarker.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add_watermark(image, text):
    logging.debug("Entered add_watermark function.")
    
    try:
        img_pil = Image.fromarray(image)
        logging.debug("Successfully converted image array to PIL Image object.")
    except Exception as e:
        logging.error(f"Failed to convert image array to PIL Image object: {e}")
        return None
    
    try:
        watermark_image = img_pil.copy()
        draw = ImageDraw.Draw(watermark_image)
        logging.debug("Created a copy of the original image for watermarking.")
    except Exception as e:
        logging.error(f"Failed to create a copy of the original image: {e}")
        return None
    
    w, h = img_pil.size
    font_size = int(min(w, h) / 6)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
        logging.debug("Loaded font successfully.")
    except Exception as e:
        logging.error(f"Failed to load font: {e}")
        return None
    
    try:
        # Create a transparent overlay using class method
        overlay = Image.new('RGBA', img_pil.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        logging.debug("Successfully created a transparent overlay.")
    except Exception as e:
        logging.error(f"Failed to create a transparent overlay: {e}")
        return None
    
    try:
        draw.text((0, 0), text, fill=(255, 255, 255, 255), font=font)
        bbox = overlay.getbbox()
        logging.debug("Watermark text drawn on overlay.")
    except Exception as e:
        logging.error(f"Failed to draw watermark text on overlay: {e}")
        return None
    
    try:
        position = (w - (bbox[2] - bbox[0]) - 100, h - (bbox[3] - bbox[1]) - 100)
        draw = ImageDraw.Draw(watermark_image)
        draw.text(position, text, fill=(255, 255, 255, 127), font=font)
        logging.debug("Watermark text drawn on the actual image.")
    except Exception as e:
        logging.error(f"Failed to draw watermark text on the actual image: {e}")
        return None
    
    logging.info("Watermark added successfully.")
    return watermark_image

iface = gr.Interface(
    fn=add_watermark,
    inputs=["image", "text"],
    outputs="image"
)

logging.info("Launching Gradio Interface.")
iface.launch()
