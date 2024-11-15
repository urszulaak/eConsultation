from views.MenuView import MenuView

class TeacherMenuView(MenuView):
    def get_menu_content(self):
        return [
            'Add consultation days [A]',
            'Check consultation request [C]',
            'Log out [ctrl + E]',
        ]

    def get_shortcuts(self):
        return {
            ord('a'): 0,
            ord('c'): 1,
        }