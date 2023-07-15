from rich.console import Console
from rich.table import Table

class Todo:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def remove(self, index):
        del self.todos[index]

    def toggle(self, index):
        self.todos[index].completed = not self.todos[index].completed

    def clear_completed(self):
        self.todos = [todo for todo in self.todos if not todo.completed]

class TodoApp:
    def __init__(self):
        self.console = Console()
        self.todo_list = TodoList()

    def run(self):
        self.display_commands()
        while True:
            self.display()
            command = input("> ")
            if command == "add":
                title = input("Title: ")
                self.todo_list.add(Todo(title))
            elif command == "remove":
                index = int(input("Index: "))
                self.todo_list.remove(index)
            elif command == "toggle":
                index = int(input("Index: "))
                self.todo_list.toggle(index)
            elif command == "clear":
                self.todo_list.clear_completed()
            elif command == "quit":
                break

    def display(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Index")
        table.add_column("Title")
        table.add_column("Completed")
        for i, todo in enumerate(self.todo_list.todos):
            table.add_row(str(i), todo.title, "Yes" if todo.completed else "No")
        self.console.print(table)

    def display_commands(self):
        self.console.print("Available commands:")
        self.console.print("[bold]add[/bold]: Add a new to-do item")
        self.console.print("[bold]remove[/bold]: Remove a to-do item by index")
        self.console.print("[bold]toggle[/bold]: Toggle the completed status of a to-do item by index")
        self.console.print("[bold]clear[/bold]: Remove all completed to-do items")
        self.console.print("[bold]quit[/bold]: Exit the app")

if __name__ == "__main__":
    app = TodoApp()
    app.run()