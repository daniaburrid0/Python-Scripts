# Import the necessary libraries
import os
import logging
import PyPDF2
import magic
from gtts import gTTS
from rich.console import Console
import argparse

console = Console()
# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def is_pdf(file_path):
    # Read first 4 bytes to determine if file is PDF
    with open(file_path, "rb") as file:
        file_start = file.read(4)
    return file_start == b"%PDF"

def extract_text_from_pdf(file_path, page='all'):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)

            if page == 'all':
                text = ''.join([pdf_reader.getPage(i).extractText() for i in range(pdf_reader.getNumPages())])
            else:
                text = pdf_reader.getPage(page).extractText()

            return text.strip()
    except (FileNotFoundError, PyPDF2.utils.PdfReadError) as e:
        logging.error(str(e))
        return None
    except Exception as e:
        logging.error(str(e))
        return None

def convert_text_to_audio(text, filename):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(f'{filename}.mp3')
    except Exception as e:
        logging.error(str(e))

def parse_args():
    parser = argparse.ArgumentParser(description='Convert a PDF to an audio file.')
    parser.add_argument('pdf', help='The path to the pdf file')
    parser.add_argument('audio', help='The name of the audio file')

    return parser.parse_args()

def main():
    args = parse_args()

    if not is_pdf(args.pdf):
        logging.error("Given file is not a PDF.")
        return

    text = extract_text_from_pdf(args.pdf)
    if text:
        convert_text_to_audio(text, args.audio)
        logging.info("The audio file has been created successfully.")
        os.remove(args.pdf)
        logging.info("PDF file removed successfully.")

if __name__ == '__main__':
    main()