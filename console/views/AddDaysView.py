from shared_core.View import View
import curses
from curses import wrapper
import time
from curses.textpad import Textbox
from views.Custom import Custom

class AddDaysView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.addDaysController = controller
        self.response = response
        self.custom = Custom

    def _content(self, stdscr, current_day, days):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        curses.curs_set(0)
        menu_height = 11
        exit = "[ctrl + E - exit]"
        line = "Choose day"
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+exit) // 2), line,curses.color_pair(4))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+exit) // 2)+len(line)+1, exit,curses.color_pair(5))
        days = self.addDaysController._getDays()
        available_width = w // len(days)
        for i, day in enumerate(days):
            x_position = available_width * i
            win_day = curses.newwin(5, available_width, menu_height+2, x_position)
            win_day.attron(curses.color_pair(3))
            win_day.box()
            win_day.attroff(curses.color_pair(3))
            text = str(day)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            if i == current_day:
                win_day.attron(curses.color_pair(5))
                win_day.addstr(text_y, text_x, str(day))
                win_day.attroff(curses.color_pair(5))
            else:
                win_day.addstr(text_y, text_x, str(day))
            win_day.refresh()

    def _timeStamps(self, stdscr, current_stamp, time_stamps, selected):
        h, w = stdscr.getmaxyx()
        menu_height = 16
        available_width = w // 7
        line = "Choose time stamps ["
        save = "S - save,"
        cancel = " C - cancel"
        sign = "]"
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+save+cancel+sign) // 2), line,curses.color_pair(4))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+save+cancel+sign) // 2)+len(line), save,curses.color_pair(8))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+save+cancel+sign) // 2)+len(line+save), cancel,curses.color_pair(5))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+save+cancel+sign) // 2)+len(line+save+cancel), sign,curses.color_pair(4))
        id = 0
        for i, stamp in enumerate(time_stamps):
            if i == 7:
                id = 0
                menu_height += 6
            x_position = available_width * id
            win_day = curses.newwin(5, available_width, menu_height + 2, x_position)
            win_day.attron(curses.color_pair(3))
            win_day.box()
            win_day.attroff(curses.color_pair(3))
            text = str(stamp)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            if i == current_stamp:
                win_day.attron(curses.color_pair(5))
                win_day.addstr(text_y, text_x, str(stamp))
                win_day.attroff(curses.color_pair(5))
            else:
                win_day.addstr(text_y, text_x, str(stamp))
            if i in selected:
                win_day.attron(curses.color_pair(6))
                win_day.box()
                win_day.addstr(text_y, text_x, str(stamp))
                win_day.attroff(curses.color_pair(6))
                if i == current_stamp:
                    win_day.attron(curses.color_pair(7))
                    win_day.addstr(text_y, text_x, str(stamp))
                    win_day.attroff(curses.color_pair(7))
            id += 1
            win_day.refresh()

    def _move(self, stdscr):
        current_day = 0
        days = self.addDaysController._getDays()
        self._content(stdscr, current_day, days)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_LEFT) and current_day > 0:
                current_day -= 1
            elif key == curses.KEY_RIGHT and current_day < len(days) - 1:
                current_day += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._moveStamps(stdscr, current_day)
            elif key == 5:
                self.addDaysController._teacherHome()
            self._content(stdscr, current_day, days)

    def _moveStamps(self, stdscr, current_day):
        current_stamp=0
        selected = arr = [x - 1 for x in self.addDaysController.ifAdded(self.response, current_day)]
        time_stamps = self.addDaysController._getTimeStamps()
        self._timeStamps(stdscr, current_stamp, time_stamps, selected)
        while 1:
            key = stdscr.getch()
            if key == curses.KEY_LEFT and current_stamp > 0:
                current_stamp -= 1
            elif key == curses.KEY_RIGHT and current_stamp < len(time_stamps) - 1:
                current_stamp += 1
            elif key == curses.KEY_UP and len(time_stamps) > current_stamp > 6:
                current_stamp -= 7
            elif key == curses.KEY_DOWN and current_stamp < len(time_stamps) - 1 and current_stamp < 7:
                current_stamp += 7
                self._timeStamps(stdscr, current_stamp, time_stamps, selected)
            elif key == curses.KEY_ENTER or key in [10, 13] and current_stamp in selected:
                selected.remove(current_stamp)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                selected.append(current_stamp)
            elif key in [ord('s'), ord('c')]:
                if key == ord('s'):
                    success = "\u2705 SUCCESSFULLY ADDED! \u2705"
                    success2 = "    SUCCESSFULLY ADDED!    "
                    self.custom.message(stdscr,success, success2,1)
                    self.addDaysController._saveTimeStamps(selected, current_day, self.response)
                    self.custom.clearContent(stdscr,17)
                    self._move(stdscr,17)
                elif key == ord('c'):
                    self.custom.clearContent(stdscr,17)
                    self._move(stdscr)
            self._timeStamps(stdscr, current_stamp, time_stamps, selected)

    def main(self):
        wrapper(self._move)

    def close(self):
        return