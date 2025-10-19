import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Гра: Вгадай число")
        self.build_widgets()
        self.reset_game()

    def build_widgets(self) -> None:
        pass
    def reset_game(self) -> None:
        pass
    def check_guess(self, event=None) -> None:
        pass

if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()