from core.View import View
import curses
from curses import wrapper
import calendar
from datetime import datetime
from curses.textpad import Textbox, rectangle
import time

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
        curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_GREEN)
        #curses.init_pair(8, 8, curses.COLOR_BLACK)
        available_height = h - menu_height - 1
        line = "Choose available teacher [ctrl + E - exit]"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
        available_width = w // len(teachers)
        for i, teacher in enumerate(teachers):
            x_position = available_width * i
            win_day = curses.newwin(5, available_width, menu_height+2, x_position)
            win_day.attron(curses.color_pair(3))
            win_day.box()
            win_day.attroff(curses.color_pair(3))
            text = str(teacher)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            if i == current_teacher:
                win_day.attron(curses.color_pair(5))
                win_day.addstr(text_y, text_x, str(teacher))
                win_day.attroff(curses.color_pair(5))
            else:
                win_day.addstr(text_y, text_x, str(teacher))
            win_day.refresh()
        stdscr.attroff(curses.color_pair(3))

    def draw_calendar(self, stdscr, year, month, daysID, selected_day=None, selected_week=None):
        h, w = stdscr.getmaxyx()
        menu_height = 18
        line = "Choose available month and [Enter - select month/day, C - cancel]"
        self._clearPart(stdscr)
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height, w // 2 - (len(line) // 2), line)
        stdscr.attroff(curses.color_pair(3))
        menu_height = 20
        title = f"\u2B9C {calendar.month_name[month]} {year} \u2B9E"
        stdscr.addstr(menu_height, w//2 - (len(title) // 2), title)

        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(days):
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(menu_height+2, (w//2-15)+ i * 4 + 2, day)
            stdscr.attroff(curses.color_pair(3))

        cal = calendar.monthcalendar(year, month)
        start_y = 1
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    continue
                color = curses.color_pair(6) if day_idx in daysID else curses.color_pair(0)

                if selected_day == day_idx and selected_week == week_idx:
                    stdscr.attron(curses.color_pair(5) | curses.A_BOLD)
                    if day_idx in daysID:
                        stdscr.attron(curses.color_pair(7) | curses.A_BOLD)
                else:
                    stdscr.attron(color)

                stdscr.addstr(menu_height + 2 + start_y, (w // 2 - 15) + day_idx * 4 + 2, str(day).rjust(2))
                stdscr.attroff(curses.color_pair(6) | curses.color_pair(5) | curses.color_pair(7) | curses.A_BOLD)

            start_y += 1
        stdscr.refresh()

    def _stamps(self, stdscr, stamps, current_stamp):
        h, w = stdscr.getmaxyx()
        menu_height = 28

        available_height = h - menu_height - 1
        line = "Choose available teacher [ctrl + E - exit]"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
        available_width = w // len(stamps)
        for i, stamp in enumerate(stamps):
            x_position = available_width * i
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
            win_day.refresh()
        stdscr.attroff(curses.color_pair(3))

    def _form(self, stdscr):
        h, w = stdscr.getmaxyx()
        menu_height = 35
        fields = []
        content = ["Topic: ","Description: "]
        box_height = (h - 28) // len(content)
        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * 2

            win = curses.newwin(3, w - 4, y, x)
            text_x = 2
            text_y = 1
            win.attron(curses.color_pair(3))
            win.addstr(text_y, text_x, row)
            win.attroff(curses.color_pair(3))
            win.refresh()

            win_text = curses.newwin(1, w - len(row) - 6, y + 1, x + len(row) + 2)
            box = Textbox(win_text)
            win_text.refresh()

            stdscr.refresh()
            while True:
                input_text = box.edit()
                win_text.refresh()
                fields.append(input_text.strip())
                break
        return fields

    def _success(self, stdscr):
        print("qwewqew")
        h, w = stdscr.getmaxyx()
        win_shadow = curses.newwin(h // 3, w // 4, h // 2 - h // 6 + 1, w // 2 - w // 8 + 1)
        win_shadow.attron(curses.color_pair(8))
        win_shadow.box()
        win_shadow.refresh()
        win_shadow.attroff(curses.color_pair(8))
        win_error = curses.newwin(h // 3, w // 4, h // 2 - h // 6, w // 2 - w // 8)
        win_error.attron(curses.color_pair(1))
        win_error.box()
        win_error.refresh()
        win_error.attroff(curses.color_pair(1))
        no_user_found = "\u2705 SUCCESSFULLY BOOKED! \u2705"
        no_user_found2 = "    SUCCESSFULLY BOOKED!    "
        curses.curs_set(0)
        stdscr.attron(curses.color_pair(6))
        stdscr.addstr(h // 2, w // 2 - (len(no_user_found) // 2) - 1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h // 2, w // 2 - (len(no_user_found2) // 2) - 1, no_user_found2)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h // 2, w // 2 - (len(no_user_found) // 2) - 1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.attroff(curses.color_pair(6))
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
            self.draw_calendar(stdscr, year, month, daysID, current_teacher)
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
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._navigate_days(stdscr, year, month, daysID, current_teacher)

    def _navigate_days(self, stdscr, year, month, daysID, current_teacher):
        selected_day = 0
        selected_week = 0
        selected_date = None

        while True:
            self.draw_calendar(stdscr, year, month, daysID, selected_day, selected_week)
            key = stdscr.getch()

            cal = calendar.monthcalendar(year, month)
            if key == curses.KEY_RIGHT:
                selected_day = (selected_day + 1) % 7
            elif key == curses.KEY_LEFT:
                selected_day = (selected_day - 1) % 7
            elif key == curses.KEY_DOWN:
                selected_week = (selected_week + 1) % len(cal)
            elif key == curses.KEY_UP:
                selected_week = (selected_week - 1) % len(cal)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                day = cal[selected_week][selected_day]
                if selected_day not in daysID:
                    pass
                    #wyswietl komunikat brak konsultacji w danym dniu i wróć do wyboru dnia
                elif day != 0:
                    selected_date = f"{year}-{month:02}-{day:02}"
                    self._moveStamps(stdscr, year, month, daysID, current_teacher, selected_date, selected_day)
            elif key == ord("c"):
                self._moveCalendar(stdscr, current_teacher)
                return

    def _moveStamps(self, stdscr, year, month, daysID, current_teacher, selected_date, selected_day):
        current_stamp = 0
        stampsID = self.chooseConsultController.getStampsID(current_teacher, selected_day)
        stamps = self.chooseConsultController.getStamps(current_teacher, selected_day)
        self._stamps(stdscr, stamps, current_stamp)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_LEFT) and current_stamp > 0:
                current_stamp -= 1
            elif key == curses.KEY_RIGHT and current_stamp < len(stamps) - 1:
                current_stamp += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                current_stamp = stampsID[current_stamp]
                form = self._form(stdscr)
                if self.chooseConsultController.form(current_teacher, selected_date, current_stamp, form, self.response):
                    print("Proba")
                    self._success(stdscr)
            elif key == ord("c"):
                self._navigate_days(stdscr, year, month, daysID, current_teacher)
            self._stamps(stdscr, stamps, current_stamp)

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