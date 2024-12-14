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

        self.main_frame = tk.Frame(self.window, bg='#f0f0f0')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.main_frame, text="Menu", font=title_font, bg='#f0f0f0', fg='#333333')
        self.title_label.pack(pady=(0, 30))

        self.button_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.button_frame.pack(expand=True, fill='both')

        self.buttons = []
        self.current_row = 0
        self.create_menu_buttons()

    def create_menu_buttons(self):
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
            btn.bind('<Enter>', lambda e: btn.configure(bg='#45a049'))
            btn.bind('<Leave>', lambda e: btn.configure(bg='#4CAF50'))
            self.buttons.append(btn)

        self.update_button_colors()

    def update_button_colors(self):
        for i, btn in enumerate(self.buttons):
            if i == self.current_row:
                btn.configure(bg='#45a049')
            else:
                btn.configure(bg='#4CAF50')

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
        return []

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()