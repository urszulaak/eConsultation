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

        self.window.title("Choose Consultation")
        self.window.geometry("700x800")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Book a Consultation", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Subtitle
        subtitle_font = font.Font(family="Helvetica", size=12)
        self.subtitle_label = tk.Label(main_frame, text="Select a Teacher",
                                       font=subtitle_font, bg='#f0f0f0', fg='#666666')
        self.subtitle_label.pack(pady=(0, 20))

        # Content frame
        self.content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        self.content_frame.pack(expand=True, fill='both')

        # Navigation buttons frame
        nav_frame = tk.Frame(main_frame, bg='#f0f0f0')
        nav_frame.pack(fill='x', pady=(20, 0))

        # Button style
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

        # Back and Next buttons
        self.back_btn = tk.Button(nav_frame, text="Back", command=self.go_back,
                                  state=tk.DISABLED, **button_style)
        self.back_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = tk.Button(nav_frame, text="Next", command=self.go_next,
                                  state=tk.DISABLED, **button_style)
        self.next_btn.pack(side=tk.RIGHT, padx=10)

        # Load initial teachers
        self.load_teachers()

    def load_teachers(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Get teachers
        teachers_ids = self.chooseConsultController._getTeachersID()
        teachers = self.chooseConsultController._getTeachers()

        # Teachers grid
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

        # Enable/disable buttons
        self.back_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)

    def select_teacher(self, teacher_id):
        self.selected_teacher = teacher_id
        self.next_btn.config(state=tk.NORMAL)
        self.load_calendar(teacher_id)

    def load_calendar(self, teacher_id):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Select a Date")
        self.current_step = 'calendar'

        # Get available days
        available_days = self.chooseConsultController._getDaysID(self.selected_teacher)

        # Calendar frame
        calendar_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        calendar_frame.pack(expand=True, fill='both')

        # Current date
        now = datetime.now()
        cal = calendar.monthcalendar(now.year, now.month)

        # Calendar display
        calendar_grid = tk.Frame(calendar_frame, bg='#f0f0f0')
        calendar_grid.pack(expand=True)

        # Month and year label
        month_label = tk.Label(calendar_grid,
                               text=f"{calendar.month_name[now.month]} {now.year}",
                               font=("Helvetica", 16, "bold"),
                               bg='#f0f0f0')
        month_label.grid(row=0, column=1, columnspan=5, pady=10)

        # Weekday headers
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for idx, day in enumerate(weekdays):
            tk.Label(calendar_grid, text=day, bg='#f0f0f0', font=("Helvetica", 10)).grid(row=1, column=idx, padx=5,
                                                                                         pady=5)

        # Populate calendar
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    continue

                day_date = date(now.year, now.month, day)

                # Check day availability and conditions
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
                        command=lambda d=day: self.select_date(d),
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

                day_btn.grid(row=week_idx + 2, column=day_idx, padx=2, pady=2)

        # Enable/disable buttons
        self.back_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

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

    def select_date(self, day):
        now = datetime.now()
        self.selected_date = f"{now.year}-{now.month:02d}-{day:02d}"
        self.load_timestamps(day - 1)

    def load_timestamps(self, day_idx):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Select a Time Slot")
        self.current_step = 'timestamps'

        # Get available timestamps
        stamps_ids = self.chooseConsultController.getStampsID(self.selected_teacher, day_idx)
        stamps = self.chooseConsultController.getStamps(self.selected_teacher, day_idx)

        # Timestamps frame
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

        # Enable/disable buttons
        self.back_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

    def select_timestamp(self, stamp_id):
        self.selected_stamp = stamp_id
        self.next_btn.config(state=tk.NORMAL)

    def load_form(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.subtitle_label.config(text="Consultation Details")
        self.current_step = 'form'

        # Form frame
        form_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        form_frame.pack(expand=True, fill='both', padx=20)

        # Topic input
        topic_label = tk.Label(form_frame, text="Consultation Topic:", bg='#f0f0f0', font=("Helvetica", 12))
        topic_label.pack(anchor='w', pady=(0, 5))
        self.topic_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=40)
        self.topic_entry.pack(pady=(0, 20))

        # Description input
        desc_label = tk.Label(form_frame, text="Description:", bg='#f0f0f0', font=("Helvetica", 12))
        desc_label.pack(anchor='w', pady=(0, 5))
        self.desc_text = tk.Text(form_frame, font=("Helvetica", 12), width=40, height=10)
        self.desc_text.pack(pady=(0, 20))

        # Enable/disable buttons
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
            # Timestamp selection
            self.load_timestamps(int(self.selected_date.split('-')[2]) - 1)
        elif self.current_step == 'timestamps':
            # Form
            self.load_form()
        elif self.current_step == 'form':
            # Submit consultation
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


