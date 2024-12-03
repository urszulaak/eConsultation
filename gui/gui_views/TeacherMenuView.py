from gui_views.MenuView import MenuView
import tkinter as tk

class TeacherMenuView(MenuView):
    def __init__(self, controller, response=None):
        super().__init__(controller, response)
        self.window.title("Teacher Menu")
        self.title_label.configure(text="Teacher Menu")

    def get_menu_content(self):
        return [
            'Add consultation days',
            'Check consultation request',
            'Log out [ctrl + E]',
        ]