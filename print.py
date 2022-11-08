from rich import print
from rich.console import Console

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

c = Console()
c.print("Terminal", "Root", style="#ccc010 bold")
t = '[red on yellow reverse] Eltinho! [/]'
c.print(t)
c.log(t)
c.print("Hello", "World!",
        style="bold red on white",
        justify='center')


c.print(
    'oshe',
    justify='full',
    style='yellow bold'
)