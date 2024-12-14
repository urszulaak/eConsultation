import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom

class HomeView(View):
    def __init__(self, controller, response=None):
        self.homeController = controller
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
        title_label = tk.Label(main_frame, text="Welcome", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(main_frame, text="Choose Your Action", font=subtitle_font, bg='#f0f0f0', fg='#666666')
        subtitle_label.pack(pady=(0, 20))

        button_style = {
        'font': font.Font(family="Segoe UI", size=max(10, int(self.window.winfo_screenwidth() * 0.01))),
        'width': max(20, int(self.window.winfo_screenwidth() * 0.025)),
        'bg': COLORS['primary'],
        'fg': COLORS['text_light'],
        'activebackground': COLORS['secondary'],
        }

        buttons = [
            ("Login", self.on_login),
            ("Register", self.on_register),
            ("Information", self.on_information),
            ("Console Version", self.on_console),
            ("Exit", self.on_quit)
        ]

        for text, command in buttons:
            btn = tk.Button(main_frame, text=text, command=command, **button_style)
            btn.pack(pady=10)
            btn.bind('<Enter>', lambda e, btn=btn: btn.configure(bg='#45a049'))
            btn.bind('<Leave>', lambda e, btn=btn: btn.configure(bg='#4CAF50'))

    def on_login(self):
        self.homeController.menuChoice(0)

    def on_register(self):
        self.homeController.menuChoice(1)

    def on_information(self):
        self.homeController.menuChoice(2)

    def on_console(self):
        self.window.destroy()
        self.homeController.menuChoice(3)

    def on_quit(self):
        self.window.destroy()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.on_quit()