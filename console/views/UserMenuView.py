from views.MenuView import MenuView

class UserMenuView(MenuView):
    def get_menu_content(self):
        return [
            'Book consultation [B]',
            'Check consultations status [C]',
            'Log out [ctrl + E]',
        ]

    def get_shortcuts(self):
        return {
            ord('b'): 0,
            ord('c'): 1,
        }
