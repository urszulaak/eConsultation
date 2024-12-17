import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom

class LoginView(View):
    def __init__(self, controller, response=None):
        self.loginController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        COLORS = {
            'background': '#F5F5F5',
            'primary': '#4CAF50',
            'secondary': '#3B963E',
            'error': '#f44336',
            'text_dark': '#333333',
            'text_light': '#FFFFFF'
        }

        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg=COLORS['background'])

        main_frame = tk.Frame(self.window, bg=COLORS['background'])
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Login", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        input_frame = tk.Frame(main_frame, bg=COLORS['background'])
        input_frame.place(relx=0.5, rely=0.5, anchor='center')

        input_font = font.Font(family="Segoe UI", size=max(10, int(self.window.winfo_screenwidth() * 0.01)))
        label_font = font.Font(family="Helvetica", size=12)
        entry_width = max(20, int(self.window.winfo_screenwidth() * 0.025))

        input_fields = [
            ("Login:", "login", False),
            ("Password:", "password", True)
        ]

        self.entries = {}
        for label_text, entry_name, is_password in input_fields:
            frame = tk.Frame(input_frame, bg=COLORS['background'])
            frame.pack(fill='x', pady=10)

            label = tk.Label(frame, text=label_text, font=label_font, anchor='w', bg=COLORS['background'], fg=COLORS['text_dark'])
            label.pack(side='left', padx=5)

            entry = tk.Entry(frame, font=input_font, width=entry_width, show='*' if is_password else '')
            entry.pack(side='right', padx=5)
            self.entries[entry_name] = entry

        login_btn = tk.Button(input_frame, text="Login", command=self.on_login,
                               font=input_font, bg=COLORS['primary'], fg=COLORS['text_light'],
                               activebackground=COLORS['secondary'], relief='flat',
                               width=entry_width)
        login_btn.pack(pady=20)
        login_btn.bind('<Enter>', lambda e: login_btn.configure(bg=COLORS['secondary']))
        login_btn.bind('<Leave>', lambda e: login_btn.configure(bg=COLORS['primary']))

        back_btn = tk.Button(input_frame, text="Back to Home", command=self.on_back,
                              font=label_font, bg=COLORS['error'], fg=COLORS['text_light'],
                              activebackground='#d32f2f', relief='flat',
                              width=entry_width // 2)
        back_btn.pack(pady=10)
        back_btn.bind('<Enter>', lambda e: back_btn.configure(bg='#d32f2f'))
        back_btn.bind('<Leave>', lambda e: back_btn.configure(bg=COLORS['error']))

        self.window.bind('<Return>', self.on_login)

    def on_login(self, event=None):
        fields = [
            self.entries['login'].get(),
            self.entries['password'].get()
        ]

        if not self.loginController.isTeacher(fields):
            messagebox.showerror("Error", "Improper Login or Password!")

    def on_back(self):
        self.loginController.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
