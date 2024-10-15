from core.View import View
import curses
from curses import wrapper

class HomeView(View):

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller
        
        

    def _window(self, stdscr):
        ascii_art = """
             _ _
        .-. | | |
        |M|_|A|N|__
        |A|a|.|.|\\ \\
        |T|r| | | \\ \\
        |H|t|M|Z|  \\ \\
        | |!| | |   \\ \\
        ''''''''''''''''
"""
        stdscr.clear()
        # stdscr.curs_set(0)
        h, w = stdscr.getmaxyx()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        text = "eConsultation"
        x = w//2 - len(ascii_art)//2
        y = h//7
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(ascii_art)
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()

    def main(self):
        wrapper(self._window)

    def close(self):
        return
    
