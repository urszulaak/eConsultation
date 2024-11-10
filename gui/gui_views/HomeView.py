import tkinter as tk
from shared_core.View import View
from tkinter import messagebox

class HomeView(View):
    def __init__(self, controller, response=None):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Home View")
        self.window.geometry("400x300")

        self.label = tk.Label(self.window, text="Welcome to the Home View!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.login_button = tk.Button(self.window, text="Login", command=self.on_login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self.window, text="Register", command=self.on_register)
        self.register_button.pack(pady=5)

        self.info_button = tk.Button(self.window, text="Information", command=self.on_information)
        self.info_button.pack(pady=5)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.on_quit)
        self.quit_button.pack(pady=20)

    def on_login(self):
        messagebox.showinfo("Login", "Navigating to Login Screen...")
        self.controller.navigate_to("login")

    def on_register(self):
        messagebox.showinfo("Register", "Navigating to Register Screen...")
        self.controller.navigate_to("register")

    def on_information(self):
        messagebox.showinfo("Information", "Navigating to Information Screen...")
        self.controller.navigate_to("information")

    def on_quit(self):
        self.window.quit()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.on_quit()