import psutil
from rich.console import Console
from rich.progress import Progress

console = Console()

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

with Progress() as progress:
    task = progress.add_task("[green]Battery:", total=100)
    for i in range(100):
        progress.update(task, completed=i)
        console.print(f"{percent}% {'(plugged in)' if plugged else ''}", end="\r")