import sys
import rich
import time

def printlyrics():
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.05),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),   
    ]





































    delays = [0.2, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5]
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == "(Rock your body)":
                rich.print(f"[orange4]{char}[/orange4]", end="")
            else:
                rich.print(f"[bold][gold3]{char}[/bold][/gold3]", end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        rich.print()
        time.sleep(delays[i])

printlyrics()