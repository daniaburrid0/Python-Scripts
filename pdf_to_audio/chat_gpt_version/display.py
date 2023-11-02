from rich.console import Console
from rich.syntax import Syntax
from rich.theme import Theme

custom_theme = Theme({"info": "dim cyan", "warning": "magenta", "error": "bold red"})
console = Console(theme=custom_theme)

def display_text(title, text):
    syntax = Syntax(text, "python", theme="monokai", line_numbers=True)
    console.print(f"[info]{title}[/info]")
    console.print(syntax)

def display_error(message):
    console.print(f"[error]Error: {message}[/error]")

def display_warning(message):
    console.print(f"[warning]Warning: {message}[/warning]")

def display_success(message):
    console.print(f"[green]{message}[/green]")
