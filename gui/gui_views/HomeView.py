import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom

class HomeView(View):
    def __init__(self, controller, response=None):
        self.homeController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("System Home")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        # Create main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Welcome", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Subtitle
        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(main_frame, text="Choose Your Action", font=subtitle_font, bg='#f0f0f0', fg='#666666')
        subtitle_label.pack(pady=(0, 20))

        # Button style
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        button_style = {
            'font': button_font,
            'width': 20,
            'bg': '#4CAF50',
            'fg': 'white',
            'activebackground': '#45a049',
            'activeforeground': 'white',
            'relief': 'flat',
            'padx': 10,
            'pady': 10
        }

        # Buttons
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