import tkinter as tk
from tkinter import font
from shared_core.View import View
from gui_views.Custom import Custom


class MenuView(View):
    def __init__(self, controller, response=None):
        self.controller = controller
        self.response = response
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("Menu")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        self.main_frame = tk.Frame(self.window, bg='#f0f0f0')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.main_frame, text="Menu", font=title_font, bg='#f0f0f0', fg='#333333')
        self.title_label.pack(pady=(0, 30))

        # Button frame
        self.button_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.button_frame.pack(expand=True, fill='both')

        # Buttons
        self.buttons = []
        self.current_row = 0
        self.create_menu_buttons()

        # Bind keyboard events
        self.window.bind('<Up>', self.move_up)
        self.window.bind('<Down>', self.move_down)
        self.window.bind('<Return>', self.select_current)
        self.window.bind('<Control-e>', self.exit_menu)

    def create_menu_buttons(self):
        # To be overridden by subclasses
        content = self.get_menu_content()
        button_font = font.Font(family="Helvetica", size=12, weight="bold")

        for text in content:
            btn = tk.Button(
                self.button_frame,
                text=text,
                font=button_font,
                bg='#4CAF50',
                fg='white',
                activebackground='#45a049',
                relief='flat',
                command=lambda idx=len(self.buttons): self.select_menu_item(idx)
            )
            btn.pack(fill='x', pady=10)
            self.buttons.append(btn)

        # Highlight first button
        self.update_button_colors()

    def update_button_colors(self):
        for i, btn in enumerate(self.buttons):
            if i == self.current_row:
                btn.configure(bg='#45a049')  # Highlighted color
            else:
                btn.configure(bg='#4CAF50')  # Normal color

    def move_up(self, event=None):
        if self.current_row > 0:
            self.current_row -= 1
            self.update_button_colors()

    def move_down(self, event=None):
        if self.current_row < len(self.buttons) - 1:
            self.current_row += 1
            self.update_button_colors()

    def select_current(self, event=None):
        self.select_menu_item(self.current_row)

    def select_menu_item(self, index):
        self.controller.menuChoice(index)

    def exit_menu(self, event=None):
        # Typically exits to last menu item (usually logout)
        self.controller.menuChoice(len(self.buttons) - 1)

    def get_menu_content(self):
        # To be overridden by subclasses
        return []

    def get_shortcuts(self):
        # To be overridden by subclasses
        return {}

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()