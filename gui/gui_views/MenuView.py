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

        COLORS = {
            'background': '#F5F5F5',
            'primary': '#4CAF50',
            'secondary': '#3B963E',
            'text_dark': '#333333',
            'text_light': '#FFFFFF'
        }

        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg=COLORS['background'])

        main_frame = tk.Frame(self.window, bg=COLORS['background'])
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Menu", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(main_frame, text="Welcome to your panel", font=subtitle_font, bg='#f0f0f0', fg='#666666')
        subtitle_label.pack(pady=(0, 20))

        button_style = {
            'font': font.Font(family="Segoe UI", size=max(10, int(self.window.winfo_screenwidth() * 0.01))),
            'width': max(20, int(self.window.winfo_screenwidth() * 0.025)),  # Same as in HomeView
            'bg': COLORS['primary'],
            'fg': COLORS['text_light'],
            'activebackground': COLORS['secondary'],
        }

        self.button_frame = tk.Frame(main_frame, bg=COLORS['background'])
        self.button_frame.pack(expand=True, fill='both')

        self.buttons = []
        self.current_row = 0
        self.create_menu_buttons(button_style)

    def create_menu_buttons(self, button_style):
        content = self.get_menu_content()

        for text in content:
            btn = tk.Button(
                self.button_frame,
                text=text,
                command=lambda idx=len(self.buttons): self.select_menu_item(idx),
                **button_style
            )
            btn.pack(pady=10)  # Remove fill='x'
            btn.bind('<Enter>', lambda e, btn=btn: btn.configure(bg='#45a049'))
            btn.bind('<Leave>', lambda e, btn=btn: btn.configure(bg='#4CAF50'))
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
        self.controller.menuChoice(len(self.buttons) - 1)

    def get_menu_content(self):
        return []

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
