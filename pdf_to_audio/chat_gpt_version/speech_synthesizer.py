from gtts import gTTS
from rich.console import Console
import os

console = Console()

def text_to_speech(text, output_file):
    try:
        tts = gTTS(text)
        tts.save(output_file)
        console.print(f"[green]Audio file saved as {output_file}[/green]")
    except Exception as e:
        console.print(f"[red]An error occurred during text-to-speech conversion: {e}[/red]")
