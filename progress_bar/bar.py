from time import sleep
from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task("[green]Counting...", total=100)

    for i in range(1, 101):
        sleep(0.1)
        progress.update(task, completed=i)

print("[bold green]Done!")