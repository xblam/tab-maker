import tkinter as tk
from tkinter import font

class GuitarTabCreator:
    def __init__(self):
        self.strings = ["e", "B", "G", "D", "A", "E"]  # Standard tuning from high to low
        self.tab = {string: ["---"] * 30 for string in self.strings}  # Initialize with 30 frets
        self.current_row = 0
        self.current_col = 0

    def display_tab(self):
        for i, string in enumerate(self.strings):
            row_text = f"{string} |"
            for col, fret in enumerate(self.tab[string]):
                if i == self.current_row and col == self.current_col:
                    row_text += f"[{fret}]"
                else:
                    row_text += f"{fret}"  # Continuous dashes without spaces

            # Update the label for the current string
            self.labels[i].config(
                text=row_text,
                bg="white",
                fg="black"
            )

    def add_fret(self, fret):
        if not fret.isdigit():
            return

        fret_str = fret.ljust(3, '-')
        current_string = self.strings[self.current_row]
        while len(self.tab[current_string]) <= self.current_col:
            for string in self.strings:
                self.tab[string].append("---")

        self.tab[current_string][self.current_col] = fret_str

    def delete_fret(self):
        current_string = self.strings[self.current_row]
        if self.current_col < len(self.tab[current_string]):
            self.tab[current_string][self.current_col] = "---"

    def move_cursor(self, direction):
        if direction == "up":
            self.current_row = (self.current_row - 1) % len(self.strings)
        elif direction == "down":
            self.current_row = (self.current_row + 1) % len(self.strings)
        elif direction == "left":
            self.current_col = max(0, self.current_col - 1)
        elif direction == "right":
            self.current_col += 1
        self.display_tab()

    def run(self):
        self.root = tk.Tk()
        self.root.title("Guitar Tab Creator")
        self.root.configure(bg="white")

        self.labels = []
        for i, string in enumerate(self.strings):
            label = tk.Label(self.root, text="", font=("Courier", 14), bg="white", fg="black", anchor="w")
            label.pack(fill="x")
            self.labels.append(label)

        self.display_tab()

        self.root.bind("<Up>", lambda e: self.move_cursor("up"))
        self.root.bind("<Down>", lambda e: self.move_cursor("down"))
        self.root.bind("<Left>", lambda e: self.move_cursor("left"))
        self.root.bind("<Right>", lambda e: self.move_cursor("right"))
        self.root.bind("<KeyPress-d>", lambda e: self.delete_fret())
        self.root.bind("<KeyPress-0>", lambda e: self.add_fret("0"))
        self.root.bind("<KeyPress-1>", lambda e: self.add_fret("1"))
        self.root.bind("<KeyPress-2>", lambda e: self.add_fret("2"))
        self.root.bind("<KeyPress-3>", lambda e: self.add_fret("3"))
        self.root.bind("<KeyPress-4>", lambda e: self.add_fret("4"))
        self.root.bind("<KeyPress-5>", lambda e: self.add_fret("5"))
        self.root.bind("<KeyPress-6>", lambda e: self.add_fret("6"))
        self.root.bind("<KeyPress-7>", lambda e: self.add_fret("7"))
        self.root.bind("<KeyPress-8>", lambda e: self.add_fret("8"))
        self.root.bind("<KeyPress-9>", lambda e: self.add_fret("9"))

        self.root.mainloop()

if __name__ == "__main__":
    tab_creator = GuitarTabCreator()
    tab_creator.run()
