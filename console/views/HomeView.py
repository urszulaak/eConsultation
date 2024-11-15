from shared_core.View import View
from shared_core.ViewFactory import ViewFactory
import curses
from curses import wrapper
from views.Custom import Custom

class HomeView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.homeController = controller
        self.custom = Custom

    def _menuBar(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        text = """


███████╗               ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝              ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗      █████╗    ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝      ╚════╝    ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████╗              ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝               ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                       

                                                                                                         

"""
        stdscr.clear()
        curses.curs_set(0)
        text_lines = text.splitlines()
        max_text_width = max(len(line) for line in text_lines)
        menu_height = -1

        text_x = w // 2 - max_text_width // 2
        for i, line in enumerate(text_lines):
            stdscr.addstr(0 + i, text_x, line,curses.color_pair(4))
            menu_height += 1

        stdscr.hline(menu_height-2 , 0, ' ', w, curses.color_pair(2))
        stdscr.refresh()
        self._move(stdscr)


    def _content(self, stdscr, current_row, content):
        self.custom.list(stdscr, current_row, content)

    def _move(self, stdscr):
        current_row = 0
        content = ['Login [L]', 'Register [R]', 'Information [I]', 'Graphic version [G]', 'Exit [ctrl + E]']
        self._content(stdscr, current_row, content)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_UP) and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.homeController.menuChoice(current_row)
            elif key in [ord('l'), ord('r'), ord('i'), ord('g')]:
                if key == ord('l'):
                    current_row = 0
                elif key == ord('r'):
                    current_row = 1
                elif key == ord('i'):
                    current_row = 2
                elif key == ord('g'):
                    current_row = 3
                self.homeController.menuChoice(current_row)
            elif key == 5:
                current_row = 4
                self.homeController.menuChoice(current_row)
            
            self._content(stdscr, current_row, content)

    def main(self):
        wrapper(self._menuBar)

    def close(self):
        return
    
