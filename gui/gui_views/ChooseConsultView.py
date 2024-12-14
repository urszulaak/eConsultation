import tkinter as tk
from tkinter import messagebox, font
from shared_core.View import View
from gui_views.Custom import Custom
import calendar
from datetime import datetime, date
import requests


class ChooseConsultView(View):
    def __init__(self, controller, response=None):
        self.chooseConsultController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)
        self.response = response
        self.holidays = {}
        self.current_step = 'teachers'
        self.selected_teacher = None
        self.selected_date = None
        self.selected_stamp = None

        COLORS = {
        'background': '#F5F5F5',
        'primary': '#4CAF50',
        'secondary': '#3B963E',
        'text_dark': '#333333',
        'text_light': '#FFFFFF'
        }

        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Book a Consultation", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        subtitle_font = font.Font(family="Helvetica", size=12)
        self.subtitle_label = tk.Label(main_frame, text="Select a Teacher", font=subtitle_font, bg='#f0f0f0', fg='#666666')
        self.subtitle_label.pack(pady=(0, 20))

        self.content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        self.content_frame.pack(expand=True, fill='both')

        nav_frame = tk.Frame(main_frame, bg='#f0f0f0')
        nav_frame.pack(fill='x', pady=(20, 0))

        button_font = font.Font(family="Helvetica", size=10, weight="bold")
        button_style = {
            'font': button_font,
            'width': 15,
            'bg': '#4CAF50',
            'fg': 'white',
            'activebackground': '#45a049',
            'activeforeground': 'white',
            'relief': 'flat',
            'padx': 10,
            'pady': 5
        }

        home_button_style = button_style.copy()
        home_button_style.update({
            'bg': '#f44336', 
            'fg': 'white',
            'activebackground': '#d32f2f'
        })

        self.home_btn = tk.Button(nav_frame, text="Back to Home", command=self.go_home, **home_button_style)
        self.home_btn.pack(side=tk.LEFT, padx=10)

        self.back_btn = tk.Button(nav_frame, text="Back", command=self.go_back, state=tk.DISABLED, **button_style)
        self.back_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = tk.Button(nav_frame, text="Next", command=self.go_next, state=tk.DISABLED, **button_style)
        self.next_btn.pack(side=tk.RIGHT, padx=10)

        self.load_teachers()

    def go_home(self):
        self.chooseConsultController.home()

    def load_teachers(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        teachers_ids = self.chooseConsultController._getTeachersID()
        teachers = self.chooseConsultController._getTeachers()

        teachers_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        teachers_frame.pack(expand=True, fill='both')

        for idx, teacher in enumerate(teachers):
            teacher_btn = tk.Button(
                teachers_frame,
                text=teacher,
                command=lambda t=teachers_ids[idx]: self.select_teacher(t),
                font=("Helvetica", 12),
                width=30,
                bg='#4CAF50',
                fg='white',
                activebackground='#45a049'
            )
            teacher_btn.pack(pady=10)

        self.back_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)

    def select_teacher(self, teacher_id):
        self.selected_teacher = teacher_id
        self.next_btn.config(state=tk.NORMAL)
        self.load_calendar(teacher_id)

    def load_calendar(self, teacher_id):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Select a Date")
        self.current_step = 'calendar'

        if not hasattr(self, 'displayed_year') or not hasattr(self, 'displayed_month'):
            now = datetime.now()
            self.displayed_year = now.year
            self.displayed_month = now.month

        available_days = self.chooseConsultController._getDaysID(self.selected_teacher)

        calendar_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        calendar_frame.pack(expand=True, fill='both')

        nav_frame = tk.Frame(calendar_frame, bg='#f0f0f0')
        nav_frame.pack(fill='x', pady=10)

        month_nav_frame = tk.Frame(nav_frame, bg='#f0f0f0')
        month_nav_frame.pack(side=tk.LEFT, expand=True)

        prev_month_btn = tk.Button(
            month_nav_frame,
            text="⬅️",  # Left arrow emoji
            command=self.prev_month,
            font=("Helvetica", 12),
            width=3,
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049'
        )
        prev_month_btn.pack(side=tk.LEFT, padx=(5, 0))  # Reduced left padding to bring closer

        month_label = tk.Label(
            month_nav_frame,
            text=f"{calendar.month_name[self.displayed_month]} {self.displayed_year}",
            font=("Helvetica", 16, "bold"),
            bg='#f0f0f0'
        )
        month_label.pack(side=tk.LEFT, padx=(5, 5))  # Reduced padding around month label

        next_month_btn = tk.Button(
            month_nav_frame,
            text="➡️",  # Right arrow emoji
            command=self.next_month,
            font=("Helvetica", 12),
            width=3,
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049'
        )
        next_month_btn.pack(side=tk.LEFT, padx=(0, 5))  # Reduced right padding to bring closer

        calendar_grid = tk.Frame(calendar_frame, bg='#f0f0f0')
        calendar_grid.pack(expand=True)

        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for idx, day in enumerate(weekdays):
            tk.Label(calendar_grid, text=day, bg='#f0f0f0', font=("Helvetica", 10)).grid(row=0, column=idx, padx=5, pady=5)

        cal = calendar.monthcalendar(self.displayed_year, self.displayed_month)
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    continue

                day_date = date(self.displayed_year, self.displayed_month, day)

                is_available = (day_idx + 1) in available_days and \
                            day_date >= date.today() and \
                            not self.is_holiday(day_date)

                day_btn_style = {
                    'width': 4,
                    'height': 2,
                    'font': ("Helvetica", 10),
                    'relief': tk.FLAT
                }

                if is_available:
                    day_btn = tk.Button(
                        calendar_grid,
                        text=str(day),
                        command=lambda d=day, idx=day_idx: self.select_date(d, idx),
                        bg='#4CAF50',
                        fg='white',
                        **day_btn_style
                    )
                else:
                    day_btn = tk.Button(
                        calendar_grid,
                        text=str(day),
                        state=tk.DISABLED,
                        bg='#CCCCCC',
                        fg='white',
                        **day_btn_style
                    )
                day_btn.grid(row=week_idx + 1, column=day_idx, padx=2, pady=2)

        self.back_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

    def prev_month(self):
        if self.displayed_month == 1:
            self.displayed_month = 12
            self.displayed_year -= 1
        else:
            self.displayed_month -= 1
        self.load_calendar(self.selected_teacher)

    def next_month(self):
        if self.displayed_month == 12:
            self.displayed_month = 1
            self.displayed_year += 1
        else:
            self.displayed_month += 1
        self.load_calendar(self.selected_teacher)

    def is_holiday(self, date):
        year = date.year
        if year not in self.holidays:
            try:
                url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL"
                response = requests.get(url)
                response.raise_for_status()
                holidays = response.json()
                self.holidays[year] = {datetime.strptime(holiday['date'], '%Y-%m-%d').date() for holiday in holidays}
            except requests.RequestException:
                self.holidays[year] = set()

        return date in self.holidays.get(year, set())

    def select_date(self, day, day_idx):
        now = datetime.now()
        self.selected_date = f"{now.year}-{now.month:02d}-{day:02d}"
        self.load_timestamps(day, day_idx)

    def load_timestamps(self, day, day_idx):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Select a Time Slot")
        self.current_step = 'timestamps'

        stamps_ids = self.chooseConsultController.getStampsID(self.selected_teacher, day_idx)
        stamps = self.chooseConsultController.getStamps(self.selected_teacher, day_idx)

        timestamps_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        timestamps_frame.pack(expand=True, fill='both')

        for idx, stamp in enumerate(stamps):
            stamp_btn = tk.Button(
                timestamps_frame,
                text=stamp,
                command=lambda s=stamps_ids[idx]: self.select_timestamp(s),
                font=("Helvetica", 12),
                width=30,
                bg='#4CAF50',
                fg='white',
                activebackground='#45a049'
            )
            stamp_btn.pack(pady=10)

        self.back_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

    def select_timestamp(self, stamp_id):
        self.selected_stamp = stamp_id
        self.load_form()

    def load_form(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Consultation Details")
        self.current_step = 'form'

        form_frame = tk.Frame(self.content_frame, bg='#f0f0f0', padx=40, pady=20)
        form_frame.pack(expand=True, fill='both', pady=(0, 10))  # Reduced bottom padding to move it closer

        topic_label = tk.Label(form_frame, text="Consultation Topic", bg='#f0f0f0', font=("Helvetica", 12))
        topic_label.grid(row=0, column=0, pady=(10, 5), sticky="ew", padx=10)  # Centered label
        self.topic_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=40)
        self.topic_entry.grid(row=1, column=0, pady=(0, 20), padx=10)  # Input field below label

        desc_label = tk.Label(form_frame, text="Description", bg='#f0f0f0', font=("Helvetica", 12))
        desc_label.grid(row=2, column=0, pady=(10, 5), sticky="ew", padx=10)  # Centered label
        self.desc_text = tk.Text(form_frame, font=("Helvetica", 12), width=40, height=10)
        self.desc_text.grid(row=3, column=0, pady=(0, 20), padx=10)  # Input field below label

        form_frame.grid_rowconfigure(0, weight=1)
        form_frame.grid_rowconfigure(1, weight=1)
        form_frame.grid_rowconfigure(2, weight=1)
        form_frame.grid_rowconfigure(3, weight=1)
        form_frame.grid_columnconfigure(0, weight=1)

        self.back_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.NORMAL)

    def go_back(self):
        if self.current_step == 'calendar':
            self.load_teachers()
        elif self.current_step == 'timestamps':
            self.load_calendar(self.selected_teacher)
        elif self.current_step == 'form':
            self.load_timestamps(int(self.selected_date.split('-')[2]) - 1)

    def go_next(self):
        if self.current_step == 'teachers':
            self.load_calendar(self.selected_teacher)
        elif self.current_step == 'calendar':
            self.load_timestamps(int(self.selected_date.split('-')[2]) - 1)
        elif self.current_step == 'form':
            topic = self.topic_entry.get()
            description = self.desc_text.get("1.0", tk.END).strip()

            if not topic or not description:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            form_data = [topic, description]
            result = self.chooseConsultController.form(
                self.selected_teacher,
                self.selected_date,
                self.selected_stamp,
                form_data,
                self.response
            )

            if result == 0:
                messagebox.showerror("Error", "Booking failed.")
            else:
                messagebox.showinfo("Success", "Consultation booked successfully!")
                self.chooseConsultController.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()