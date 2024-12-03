from gui_views.MenuView import MenuView
import tkinter as tk

class UserMenuView(MenuView):
    def __init__(self, controller, response=None):
        super().__init__(controller, response)
        self.window.title("User Menu")
        self.title_label.configure(text="User Menu")

    def get_menu_content(self):
        return [
            'Book consultation',
            'Check consultations status',
            'Log out [ctrl + E]',
        ]