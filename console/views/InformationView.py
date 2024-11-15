from shared_core.View import View
import curses
from curses import wrapper
from views.Custom import Custom

class InformationView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.informationController = controller
        self.custom = Custom

    def _content(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        curses.curs_set(0)
        menu_height = 11
        exit_text = "Exit [ctrl+E]"
        stdscr.addstr(menu_height+1, w//2-(len(exit_text)//2), exit_text,curses.color_pair(5))
        menu_height = 13
        desc = "Consultation management application"
        content = ["As a student you can:","\u2022 Book consultations","\u2022 Check current consutations",
                   "As a teacher you can:","\u2022 Add consultations schedule","\u2022 Check current consutations"]
        stdscr.addstr(menu_height+1, w//2-(len(desc)//2), desc,curses.color_pair(1))
        menu_height = 16
        for i in range(0,len(content)):
            if content[i][0] == "A":
                stdscr.addstr(menu_height+i*2, 4,content[i],curses.color_pair(4))
            else:
                stdscr.addstr(menu_height+i*2, 6,content[i])
        while 1:
            key = stdscr.getch()
            if key == 5:
                self.informationController.home()

    def _clearContent(self, stdscr):
        h, w = stdscr.getmaxyx()
        menu_height = 10
        start_y = menu_height + 1
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()


    def main(self):
        wrapper(self._content)

    def close(self):
        return
    