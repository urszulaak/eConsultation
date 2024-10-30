from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class ChooseConsultView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.chooseConsultController = controller
        self.response = response

    def _content(self, stdscr, current_teacher, teachers):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 10

        #curses.init_color(8,220,220,220)

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_GREEN)
        #curses.init_pair(8, 8, curses.COLOR_BLACK)
        available_height = h - menu_height - 1
        line = "Choose available teacher [ctrl + E - exit]"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
        stdscr.attroff(curses.color_pair(3))
        stdscr.attron(curses.color_pair(3))
        available_width = w // len(teachers)
        for i, day in enumerate(teachers):
            x_position = available_width * i
            win_day = curses.newwin(5, available_width, menu_height+2, x_position)
            win_day.attron(curses.color_pair(3))
            win_day.box()
            win_day.attroff(curses.color_pair(3))
            text = str(day)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            if i == current_teacher:
                win_day.attron(curses.color_pair(5))
                win_day.addstr(text_y, text_x, str(day))
                win_day.attroff(curses.color_pair(5))
            else:
                win_day.addstr(text_y, text_x, str(day))
            win_day.refresh()

    def _days(self, stdscr,current_day, days):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 16
        available_height = h - menu_height - 1
        line = "Choose available day [ctrl + E - exit]"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
        stdscr.attroff(curses.color_pair(3))
        stdscr.attron(curses.color_pair(3))
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

    # def _timeStamps(self, stdscr, current_stamp, time_stamps, selected):
    #     h, w = stdscr.getmaxyx()
    #     menu_height = 16
    #     available_height = h - menu_height - 1
    #     available_width = w // 7
    #     line = "Choose time stamps [S - save, C - cancel]"
    #     stdscr.attron(curses.color_pair(3))
    #     stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
    #     stdscr.attroff(curses.color_pair(3))
    #     id=0
    #     for i, stamp in enumerate(time_stamps):
    #         if i == 7:
    #             id=0
    #             menu_height += 6
    #         x_position = available_width * id
    #         win_day = curses.newwin(5, available_width, menu_height + 2, x_position)
    #         win_day.attron(curses.color_pair(3))
    #         win_day.box()
    #         win_day.attroff(curses.color_pair(3))
    #         text = str(stamp)
    #         text_x = (available_width - len(text)) // 2
    #         text_y = 5 // 2
    #         if i == current_stamp:
    #             win_day.attron(curses.color_pair(5))
    #             win_day.addstr(text_y, text_x, str(stamp))
    #             win_day.attroff(curses.color_pair(5))
    #         else:
    #             win_day.addstr(text_y, text_x, str(stamp))
    #         if i in selected:
    #             win_day.attron(curses.color_pair(6))
    #             win_day.box()
    #             win_day.addstr(text_y, text_x, str(stamp))
    #             win_day.attroff(curses.color_pair(6))
    #             if i == current_stamp:
    #                 win_day.attron(curses.color_pair(7))
    #                 win_day.addstr(text_y, text_x, str(stamp))
    #                 win_day.attroff(curses.color_pair(7))
    #         id +=1
    #         win_day.refresh()

    def _moveTeacher(self, stdscr):
        current_teacher = 0
        teachersID = self.chooseConsultController._getTeachersID()
        teachers = self.chooseConsultController._getTeachers()
        self._content(stdscr, current_teacher, teachers)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_LEFT) and current_teacher > 0:
                current_teacher -= 1
            elif key == curses.KEY_RIGHT and current_teacher < len(teachers) - 1:
                current_teacher += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                current_teacher = teachersID[current_teacher]
                print(current_teacher)
                self._moveDay(stdscr, current_teacher)
            elif key == 5:
                self._clearContent(stdscr)
                self.chooseConsultController._userHome()
            self._content(stdscr, current_teacher, teachers)

    def _moveDay(self, stdscr, current_teacher):
        current_day = 0
        daysID = self.chooseConsultController._getDaysID(current_teacher)
        days = self.chooseConsultController._getDays(current_teacher)
        #self._days(stdscr,current_day, days)
        while 1:
            key = stdscr.getch()
            # if key == (curses.KEY_LEFT) and current_teacher > 0:
            #     current_teacher -= 1
            # elif key == curses.KEY_RIGHT and current_teacher < len(teachers) - 1:
            #     current_teacher += 1
            # elif key == curses.KEY_ENTER or key in [10, 13]:
            #     self._moveDays(stdscr, current_teacher)
            # elif key == 5:
            #     self._clearContent(stdscr)
            #     self.chooseConsultController._userHome()
            # self._content(stdscr, current_teacher, teachers)

    def _moveStamps(self, stdscr, current_day):
        current_stamp=0
        selected = []
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
                    self.addDaysController._saveTimeStamps(selected,current_day,self.response)
                    self._clearPart(stdscr)
                    self._move(stdscr)
                elif key == ord('c'):
                    self._clearPart(stdscr)
                    self._move(stdscr)
            self._timeStamps(stdscr, current_stamp, time_stamps, selected)

    def _clearPart(self, stdscr):
        h, w = stdscr.getmaxyx()
        start_y = 17
        end_y = h
        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def _clearContent(self, stdscr):
        h, w = stdscr.getmaxyx()
        start_y = 11
        end_y = h
        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def main(self):
        wrapper(self._moveTeacher)

    def close(self):
        return