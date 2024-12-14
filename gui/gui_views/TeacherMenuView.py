import customtkinter as ctk
from customtkinter import N
from gui_views.MenuView import MenuView
import tkinter as tk

class TeacherMenuView(MenuView):
    def __init__(self, controller, response=None):
        super().__init__(controller, response)
        self.window.title('eConsultation')

    def get_menu_content(self):
        return ['Add consultation days', 'Check consultation request', 'Log out']