from PyPDF2 import PdfReader
from rich.console import Console

console = Console()

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text_content = []

        for page in reader.pages:
            text_content.append(page.extract_text())

        return "\n".join(text_content)

    except Exception as e:
        console.print(f"[red]An error occurred while reading the PDF: {e}[/red]")
        return None
