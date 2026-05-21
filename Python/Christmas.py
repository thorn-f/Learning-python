import time
import random
import sys
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

console = Console()

tree_structure = [
    "       * ", 
    "      *** ",
    "     ***** ",
    "    ******* ",
    "   ********* ",
    "  *********** ",
    " ************* ",
    "***************",
    "      |||      ",
    "      |||      "
]  

colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def get_tree():
    """Generates the tree with randomized star colors."""
    tree_text = Text()
    for row in tree_structure:
        for char in row:
            if char == "*":
                tree_text.append(char, style=f"bold {random.choice(colors)}")
            elif char == "|":
                tree_text.append(char, style="bold yellow")
            else:
                tree_text.append(char)
        tree_text.append("\n")
    # Wrap in a Panel to keep it contained
    return Panel(tree_text, border_style="green", expand=False)

def run_performance():
    lines = [
        ("Oh, I don't want a lot for Christmas", 0.08, 0.3),
        ("This is all I'm asking for", 0.075, 0.25),
        ("I just wanna see my baby", 0.10, 0.3),
        ("Standing right outside my door", 0.08, 1.2),
        ("Oh, I just want you for my own", 0.11, 0.35),
        ("More than you could ever know", 0.095, 0.3),
        ("Make my wish come true", 0.075, 0.4),
        ("Oh, baby, all I want for Christmas is you", 0.115, 2.5)
    ]

    # Initialize Layout
    layout = Layout()
    layout.split_row(
        Layout(name="tree", size=25),
        Layout(name="lyrics")
    )

    full_lyrics_text = Text()

    # Use Live to handle the screen refresh automatically
    with Live(layout, screen=True, refresh_per_second=10) as live:
        for line_content, char_delay, line_pause in lines:
            current_line_text = ""
            
            for char in line_content:
                current_line_text += char
                
                # Update the content of both sections
                layout["tree"].update(get_tree())
                layout["lyrics"].update(
                    # Combine old lines with the one currently being typed
                    Text.assemble(full_lyrics_text, Text(current_line_text, style="bold green4"))
                )
                time.sleep(char_delay)
            
            # Line finished, add it to the permanent buffer and wait
            full_lyrics_text.append(current_line_text + "\n", style="bold green4")
            time.sleep(line_pause)

if __name__ == "__main__":
    try:
        run_performance()
    except KeyboardInterrupt:
        pass  