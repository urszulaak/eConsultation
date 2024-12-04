import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom


class RegisterView(View):
    def __init__(self, controller, response=None):
        self.registerController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("User Registration")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Create Account", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Input style
        input_font = font.Font(family="Helvetica", size=12)
        label_font = font.Font(family="Helvetica", size=10)

        # Account Type
        account_type_frame = tk.Frame(main_frame, bg='#f0f0f0')
        account_type_frame.pack(fill='x', pady=10)

        account_type_label = tk.Label(account_type_frame, text="Account Type:", font=label_font, bg='#f0f0f0')
        account_type_label.pack(side='left')

        self.account_type_var = tk.StringVar(value="student")
        account_type_student = tk.Radiobutton(account_type_frame, text="Student", variable=self.account_type_var,
                                              value="student", font=input_font, bg='#f0f0f0')
        account_type_teacher = tk.Radiobutton(account_type_frame, text="Teacher", variable=self.account_type_var,
                                              value="t", font=input_font, bg='#f0f0f0')
        account_type_student.pack(side='right', padx=10)
        account_type_teacher.pack(side='right')

        # Input fields
        input_fields = [
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Login:", "login"),
            ("Password:", "password")
        ]

        self.entries = {}
        for label_text, entry_name in input_fields:
            frame = tk.Frame(main_frame, bg='#f0f0f0')
            frame.pack(fill='x', pady=10)

            label = tk.Label(frame, text=label_text, font=label_font, width=15, anchor='w', bg='#f0f0f0')
            label.pack(side='left')

            entry = tk.Entry(frame, font=input_font, width=20, show='*' if entry_name == 'password' else '')
            entry.pack(side='right')
            self.entries[entry_name] = entry

        # Register Button
        register_btn = tk.Button(main_frame, text="Register", command=self.on_register,
                                 font=input_font, bg='#4CAF50', fg='white',
                                 activebackground='#45a049', relief='flat',
                                 padx=10, pady=10)
        register_btn.pack(pady=20)
        register_btn.bind('<Enter>', lambda e: register_btn.configure(bg='#45a049'))
        register_btn.bind('<Leave>', lambda e: register_btn.configure(bg='#4CAF50'))

        # Back to Home
        back_btn = tk.Button(main_frame, text="Back to Home", command=self.on_back,
                             font=label_font, bg='#f44336', fg='white',
                             activebackground='#d32f2f', relief='flat',
                             padx=10, pady=5)
        back_btn.pack(pady=10)
        back_btn.bind('<Enter>', lambda e: back_btn.configure(bg='#d32f2f'))
        back_btn.bind('<Leave>', lambda e: back_btn.configure(bg='#f44336'))

    def on_register(self):
        # Collect registration data
        fields = [
            self.account_type_var.get(),
            self.entries['first_name'].get(),
            self.entries['last_name'].get(),
            self.entries['login'].get(),
            self.entries['password'].get()
        ]

        if self.registerController.add(fields):
            messagebox.showinfo("Success", "Account created successfully!")
            self.registerController.added()
        else:
            messagebox.showerror("Error", "User with this login already exists!")

    def on_back(self):
        from gui_views.HomeView import HomeView
        HomeView(self.registerController)

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()