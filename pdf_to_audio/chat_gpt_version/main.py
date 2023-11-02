import os
from pdf_processor import extract_text_from_pdf
from speech_synthesizer import text_to_speech
from display import display_text, display_error, display_success
from rich.prompt import Prompt

def main():
    # Using Rich prompt for user input
    pdf_path = Prompt.ask("[yellow]Enter the path to your PDF file[/yellow]")

    if not os.path.isfile(pdf_path):
        display_error("The file path provided does not exist. Please check and try again.")
        return

    if not pdf_path.lower().endswith('.pdf'):
        display_error("The file provided is not a PDF. Please provide a valid PDF file.")
        return

    # Extract text from the provided PDF path
    text = extract_text_from_pdf(pdf_path)
    if text is None:
        display_error("Failed to extract text from the PDF.")
        return
    
    # Display extracted text
    display_text("Extracted Text", text)

    # Convert and save the extracted text to an MP3 file
    output_file = f"{os.path.splitext(pdf_path)[0]}.mp3"
    text_to_speech(text, output_file)

    # Final success message
    display_success(f"The text has been successfully converted to speech and saved as {output_file}")

if __name__ == "__main__":
    main()
