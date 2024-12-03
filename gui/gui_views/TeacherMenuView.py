from gui_views.MenuView import MenuView
import tkinter as tk

class TeacherMenuView(MenuView):
    def __init__(self, controller, response=None):
        super().__init__(controller, response)
        self.window.title("Teacher Menu")
        self.title_label.configure(text="Teacher Menu")

        # Bind additional keyboard shortcuts
        self.window.bind('a', lambda event: self.select_menu_item(0))
        self.window.bind('c', lambda event: self.select_menu_item(1))

    def get_menu_content(self):
        return [
            'Add consultation days [A]',
            'Check consultation request [C]',
            'Log out [ctrl + E]',
        ]

    def get_shortcuts(self):
        return {
            'a': 0,
            'c': 1,
        }