from rich.console import Console

class Rich:
    def print(self, text):
        Console().print(f"{text}", style="bold cyan")
