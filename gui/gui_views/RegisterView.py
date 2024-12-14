import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom

class RegisterView(View):
    def __init__(self, controller, response=None):
        self.registerController = controller
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
        main_frame.pack(expand=True, fill='both')

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Create Account", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        input_frame = tk.Frame(main_frame, bg=COLORS['background'])
        input_frame.place(relx=0.5, rely=0.5, anchor='center')

        input_font = font.Font(family="Segoe UI", size=max(10, int(self.window.winfo_screenwidth() * 0.01)))
        label_font = font.Font(family="Helvetica", size=12)
        entry_width = max(20, int(self.window.winfo_screenwidth() * 0.025))

        account_type_frame = tk.Frame(input_frame, bg=COLORS['background'])
        account_type_frame.pack(fill='x', pady=10)

        account_type_label = tk.Label(account_type_frame, text="Account Type:", font=label_font, bg=COLORS['background'], fg=COLORS['text_dark'])
        account_type_label.pack(side='left', padx=5)

        self.account_type_var = tk.StringVar(value="student")
        account_type_student = tk.Radiobutton(account_type_frame, text="Student", variable=self.account_type_var,
                                              value="student", font=input_font, bg=COLORS['background'], fg=COLORS['text_dark'],
                                              selectcolor=COLORS['background'])
        account_type_teacher = tk.Radiobutton(account_type_frame, text="Teacher", variable=self.account_type_var,
                                              value="t", font=input_font, bg=COLORS['background'], fg=COLORS['text_dark'],
                                              selectcolor=COLORS['background'])
        account_type_student.pack(side='right', padx=5)
        account_type_teacher.pack(side='right', padx=5)

        input_fields = [
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Login:", "login"),
            ("Password:", "password")
        ]

        self.entries = {}
        for label_text, entry_name in input_fields:
            frame = tk.Frame(input_frame, bg=COLORS['background'])
            frame.pack(fill='x', pady=10)

            label = tk.Label(frame, text=label_text, font=label_font, anchor='w', bg=COLORS['background'], fg=COLORS['text_dark'])
            label.pack(side='left', padx=5)

            entry = tk.Entry(frame, font=input_font, width=entry_width, show='*' if entry_name == 'password' else '')
            entry.pack(side='right', padx=5)
            self.entries[entry_name] = entry

        register_btn = tk.Button(input_frame, text="Register", command=self.on_register,
                                 font=input_font, bg=COLORS['primary'], fg=COLORS['text_light'],
                                 activebackground=COLORS['secondary'], relief='flat',
                                 width=entry_width)
        register_btn.pack(pady=20)
        register_btn.bind('<Enter>', lambda e: register_btn.configure(bg=COLORS['secondary']))
        register_btn.bind('<Leave>', lambda e: register_btn.configure(bg=COLORS['primary']))

        back_btn = tk.Button(input_frame, text="Back to Home", command=self.on_back,
                              font=label_font, bg=COLORS['error'], fg=COLORS['text_light'],
                              activebackground='#d32f2f', relief='flat',
                              width=entry_width // 2)
        back_btn.pack(pady=10)
        back_btn.bind('<Enter>', lambda e: back_btn.configure(bg='#d32f2f'))
        back_btn.bind('<Leave>', lambda e: back_btn.configure(bg=COLORS['error']))

        self.window.bind('<Return>', self.on_register)

    def on_register(self, event=None):
        fields = [
            self.account_type_var.get(),
            self.entries['first_name'].get(),
            self.entries['last_name'].get(),
            self.entries['login'].get(),
            self.entries['password'].get()
        ]

        if any(field == "" for field in fields):
            messagebox.showerror("Error", "All fields must be filled!")
            return

        if self.registerController.add(fields):
            messagebox.showinfo("Success", "Account created successfully!")
            self.registerController.added()
        else:
            messagebox.showerror("Error", "User with this login already exists!")

    def on_back(self):
        self.registerController.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
