import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom

class LoginView(View):
    def __init__(self, controller, response=None):
        self.loginController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("User Login")
        self.window.geometry("500x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Login", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Input style
        input_font = font.Font(family="Helvetica", size=12)
        label_font = font.Font(family="Helvetica", size=10)

        # Input fields
        input_fields = [
            ("Login:", "login", False),
            ("Password:", "password", True)
        ]

        self.entries = {}
        for label_text, entry_name, is_password in input_fields:
            frame = tk.Frame(main_frame, bg='#f0f0f0')
            frame.pack(fill='x', pady=10)

            label = tk.Label(frame, text=label_text, font=label_font, width=15, anchor='w', bg='#f0f0f0')
            label.pack(side='left')

            entry = tk.Entry(frame, font=input_font, width=20,
                             show='*' if is_password else '')
            entry.pack(side='right')
            self.entries[entry_name] = entry

        # Login Button
        login_btn = tk.Button(main_frame, text="Login", command=self.on_login,
                               font=input_font, bg='#4CAF50', fg='white',
                               activebackground='#45a049', relief='flat',
                               padx=10, pady=10, width=20)
        login_btn.pack(pady=20)
        login_btn.bind('<Enter>', lambda e: login_btn.configure(bg='#45a049'))
        login_btn.bind('<Leave>', lambda e: login_btn.configure(bg='#4CAF50'))

        # Back to Home Button
        back_btn = tk.Button(main_frame, text="Back to Home", command=self.on_back,
                              font=label_font, bg='#f44336', fg='white',
                              activebackground='#d32f2f', relief='flat',
                              padx=10, pady=5)
        back_btn.pack(pady=10)
        back_btn.bind('<Enter>', lambda e: back_btn.configure(bg='#d32f2f'))
        back_btn.bind('<Leave>', lambda e: back_btn.configure(bg='#f44336'))

    def on_login(self):
        # Collect login data
        fields = [
            self.entries['login'].get(),
            self.entries['password'].get()
        ]

        # Check login and handle different scenarios
        self.loginController.isTeacher(fields)

    def on_back(self):
        from gui_views.HomeView import HomeView
        HomeView(self.loginController)

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()