from core.View import View
import curses
from curses import wrapper
import calendar
from datetime import datetime
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
        stdscr.attroff(curses.color_pair(3))

    def draw_calendar(self, stdscr, year, month, daysID):
        h, w = stdscr.getmaxyx()
        menu_height = 18
        self._clearPart(stdscr)
        title = f"{calendar.month_name[month]} {year}"
        stdscr.addstr(menu_height, w//2 - (len(title) // 2), title)

        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(days):
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(menu_height+2, (w//2-15)+ i * 4 + 2, day)
            stdscr.attroff(curses.color_pair(3))


        cal = calendar.monthcalendar(year, month)
        start_y = 1
        for week in cal:
            for i, day in enumerate(week):
                if day == 0:
                    continue
                if i in daysID:
                    stdscr.attron(curses.color_pair(6))
                    stdscr.addstr(menu_height + 2 + start_y, (w // 2 - 15) + i * 4 + 2, str(day).rjust(2))
                    stdscr.attroff(curses.color_pair(6))
                else:
                    stdscr.addstr(menu_height+2+start_y, (w//2-15)+ i * 4 + 2, str(day).rjust(2))
            start_y += 1

        stdscr.refresh()

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
                self._moveCalendar(stdscr, current_teacher)
            elif key == 5:
                self._clearContent(stdscr)
                self.chooseConsultController._userHome()
            self._content(stdscr, current_teacher, teachers)

    def _moveCalendar(self, stdscr, current_teacher):
        daysID = self.chooseConsultController._getDaysID(current_teacher)
        #days = self.chooseConsultController._getDays(current_teacher)
        current_date = datetime.now()
        year, month = current_date.year, current_date.month
        while 1:
            self.draw_calendar(stdscr, year, month, daysID)
            key = stdscr.getch()
            if key == curses.KEY_RIGHT:
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            elif key == curses.KEY_LEFT:
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
            elif key == ord("c"):
                self._clearPart(stdscr)
                self._moveTeacher(stdscr)

    def _clearPart(self, stdscr):
        h, w = stdscr.getmaxyx()
        start_y = 18
        end_y = h
        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def _clearLowerPart(self, stdscr):
        h, w = stdscr.getmaxyx()
        start_y = 23
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