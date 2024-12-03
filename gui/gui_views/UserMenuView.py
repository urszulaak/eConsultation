from gui_views.MenuView import MenuView
import tkinter as tk

class UserMenuView(MenuView):
    def __init__(self, controller, response=None):
        super().__init__(controller, response)
        self.window.title("User Menu")
        self.title_label.configure(text="User Menu")

        # Bind additional keyboard shortcuts
        self.window.bind('b', lambda event: self.select_menu_item(0))
        self.window.bind('c', lambda event: self.select_menu_item(1))

    def get_menu_content(self):
        return [
            'Book consultation [B]',
            'Check consultations status [C]',
            'Log out [ctrl + E]',
        ]

    def get_shortcuts(self):
        return {
            'b': 0,
            'c': 1,
        }