import tkinter as tk
import subprocess
import sys

# Cesta k testom
scripts = {
    "Základná": "tests/test_a1.py",
    "Komplikovanejšia": "tests/test_a2.py",
    "Zložitá": "tests/test_a3.py",
    "Chybná": "tests/test_a4.py",
    "Neexistujúca": "tests/test_a5.py"
}

def run_script(path):
    # Spustí skript ako samostatný Python proces
    subprocess.run([sys.executable, path])

# GUI okno
root = tk.Tk()
root.title("Simulator autonómneho auta")

tk.Label(root, text="Vyber trasu:").pack(pady=10)

for name, path in scripts.items():
    btn = tk.Button(root, text=name, width=20, command=lambda p=path: run_script(p))
    btn.pack(pady=5)

root.mainloop()
