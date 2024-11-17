from shared_core.View import View
import curses
from curses import wrapper
import calendar
from datetime import datetime
from views.Custom import Custom
from curses.textpad import Textbox, rectangle
import time
import requests
import json

class ChooseConsultView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.chooseConsultController = controller
        self.response = response
        self.custom = Custom
        self.holidays = {}

    def fetch_holidays(self, year):
        if year in self.holidays:
            return
        try:
            url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL"
            response = requests.get(url)
            response.raise_for_status()
            holidays = response.json()

            self.holidays[year] = {datetime.strptime(holiday['date'], '%Y-%m-%d').date(): holiday['name'] for holiday in holidays}
        except requests.RequestException as e:
            self.holidays[year] = {}

    def is_holiday(self, date):
        return date in self.holidays.get(date.year, {})


    def _content(self, stdscr, current_teacher, teachers):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        curses.curs_set(0)
        menu_height = 11
        exit = "[ctrl + E - exit]"
        line = "Choose avaible teacher"
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+exit) // 2), line,curses.color_pair(4))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+exit) // 2)+len(line)+1, exit,curses.color_pair(5))
        menu_height = 11
        self.custom.row(stdscr, teachers, menu_height, current_teacher)
        if not teachers:
            no_consult_found = "\u274c NO TEACHERS FOUND! \u274c"
            no_consult_found2 = "    NO TEACHERS FOUND!    "
            self.custom.message(stdscr, no_consult_found, no_consult_found2, 0)
            self.chooseConsultController.home()
            self.custom.row(stdscr, teachers, menu_height, current_teacher)

    def draw_calendar(self, stdscr, year, month, daysID, selected_day=None, selected_week=None):
        h, w = stdscr.getmaxyx()
        menu_height = 18
        line = "Choose available month and ["
        enter = "Enter - select month and then day"
        cancel = " C - cancel"
        sign = "]"
        self.custom.clearContent(stdscr,18)
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+enter+cancel+sign) // 2), line,curses.color_pair(4))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+enter+cancel+sign) // 2)+len(line), enter,curses.color_pair(8))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+enter+cancel+sign) // 2)+len(line+enter), cancel,curses.color_pair(5))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+enter+cancel+sign) // 2)+len(line+enter+cancel), sign,curses.color_pair(4))

        menu_height = 20
        title = f"\u2B9C {calendar.month_name[month]} {year} \u2B9E"
        stdscr.addstr(menu_height, w//2 - (len(title) // 2), title, curses.color_pair(3))

        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(days):
            stdscr.addstr(menu_height+1, (w//2-15) + i * 4 + 2, day,curses.color_pair(4))

        cal = calendar.monthcalendar(year, month)
        self.fetch_holidays(year)
        today = datetime.now().date()
        start_y = 1
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    continue
                color = curses.color_pair(8) if day_idx+1 in daysID else curses.color_pair(11)
                day_date = datetime(year, month, day).date()
                
                if day_date < today or day_idx + 1 not in daysID or self.is_holiday(day_date):
                    color = curses.color_pair(11)
                else:
                    color = curses.color_pair(8)

                if selected_day == day_idx and selected_week == week_idx:
                    stdscr.attron(curses.color_pair(12) | curses.A_BOLD)
                    if day_date >= today and day_idx + 1 in daysID:
                        stdscr.attron(curses.color_pair(9) | curses.A_BOLD)
                else:
                    stdscr.attron(color)

                stdscr.addstr(menu_height + 1 + start_y, (w // 2 - 15) + day_idx * 4 + 2, str(day).rjust(2))
                stdscr.attroff(curses.color_pair(8) | curses.color_pair(11) | curses.A_BOLD)

            start_y += 1
        stdscr.refresh()

    def _stamps(self, stdscr, stamps, current_stamp):
        h, w = stdscr.getmaxyx()
        menu_height = 27
        line = "Choose available time ["
        cancel = "C - cancel"
        line2 = "]"
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+cancel+line2) // 2), line,curses.color_pair(4))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+cancel+line2) // 2)+len(line)+1, cancel,curses.color_pair(5))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line+cancel+line2) // 2)+len(line+cancel)+1, line2,curses.color_pair(4))
        self.custom.row(stdscr, stamps, menu_height, current_stamp)

    def _form(self, stdscr):
        curses.curs_set(1)
        content = ["Topic: ","Description: "]
        return self.custom.input(stdscr, content, None, 35)

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
                self.chooseConsultController.home()
            self._content(stdscr, current_teacher, teachers)

    def _moveCalendar(self, stdscr, current_teacher):
        daysID = self.chooseConsultController._getDaysID(current_teacher)
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
                self.custom.clearContent(stdscr, 18)
                self._moveTeacher(stdscr)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._navigate_days(stdscr, year, month, daysID, current_teacher)

    def _navigate_days(self, stdscr, year, month, daysID, current_teacher):
        selected_day = 0
        selected_week = 0
        selected_date = None
        today = datetime.now().date()
        day_date = None

        cal = calendar.monthcalendar(year, month)
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day != 0:
                    selected_day = day_idx
                    selected_week = week_idx
                    break
            if selected_day is not None:
                break

        while True:
            self.draw_calendar(stdscr, year, month, daysID, selected_day, selected_week)
            key = stdscr.getch()

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
                day_date = datetime(year, month, day).date()
                if selected_day+1 not in daysID or day_date<today or self.is_holiday(day_date):
                    pass
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
                if form == -1:
                    self.chooseConsultController.home()
                elif self.chooseConsultController.form(current_teacher, selected_date, current_stamp, form, self.response) != 0:
                    booked = "\u2705 SUCCESSFULLY BOOKED! \u2705"
                    booked2 = "   SUCCESSFULLY BOOKED!   "
                    self.custom.message(stdscr, booked, booked2, 1)
                    self.chooseConsultController.home()
            elif key == ord("c"):
                self._navigate_days(stdscr, year, month, daysID, current_teacher)
            self._stamps(stdscr, stamps, current_stamp)

    def main(self):
        wrapper(self._moveTeacher)

    def close(self):
        return