import tkinter as tk

class Custom():

    @staticmethod
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    @staticmethod
    def get_window():
        if not tk._default_root:
            return tk.Tk()
        return tk._default_root