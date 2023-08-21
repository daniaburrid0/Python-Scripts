from PIL import Image
from rich.table import Table
from rich.console import Console

def print_exif_data(exif_data):
    # Create a table to display the EXIF data
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Tag", style="dim")
    table.add_column("Value")

    # Add each tag and its value to the table
    for tag, value in exif_data.items():
        table.add_row(str(tag), str(value))

    # Print the table using the rich library
    console = Console()
    console.print(table)
    
def extract_exif_info(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    print_exif_data(exif_data)
    
def main():
    # ask for the image path
    image_path = input("Enter the image path: ")
    extract_exif_info(image_path)
    
if __name__ == "__main__":
    main()