import tkinter as tk
from tkinter import font, messagebox, ttk
from shared_core.View import View
from gui_views.Custom import Custom
import math

class AddDaysView(View):
    def __init__(self, controller, response=None):
        self.addDaysController = controller
        self.response = response
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        COLORS = {
        'background': '#F5F5F5',
        'primary': '#4CAF50',
        'secondary': '#3B963E',
        'text_dark': '#333333',
        'text_light': '#FFFFFF'
        }
        
        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f4f4f8')

        main_frame = tk.Frame(self.window, bg='#f4f4f8')
        main_frame.pack(expand=True, fill='both', padx=30, pady=30)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Add Course Days", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        days_frame = tk.Frame(main_frame, bg='#f4f4f8')
        days_frame.pack(pady=20)

        days_label = tk.Label(days_frame, text="Select Day", font=("Segoe UI", 16, "bold"), bg='#f4f4f8', fg='#2c3e50')
        days_label.pack(pady=(0, 15))

        self.days = self.addDaysController._getDays()
        self.selected_day_index = tk.IntVar()
        self.day_buttons = []

        days_button_frame = tk.Frame(days_frame, bg='#f4f4f8')
        days_button_frame.pack()

        for day_index, day_name in enumerate(self.days, 1):
            btn = tk.Button(
                days_button_frame,
                text=day_name,
                command=lambda idx=day_index: self.on_day_select(idx),
                font=("Segoe UI", 12, "bold"),
                bg='#2ecc71',
                fg='white',
                activebackground='#27ae60',
                relief='flat',
                width=10,
                padx=10,
                pady=8,
                borderwidth=0
            )
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            self.day_buttons.append(btn)

        self.timestamps_frame = tk.Frame(main_frame, bg='#f4f4f8')
        self.timestamps_frame.pack(pady=20)

        bottom_frame = tk.Frame(main_frame, bg='#f4f4f8')
        bottom_frame.pack(pady=20)

        button_style = {
            'font': ("Segoe UI", 12, "bold"),
            'fg': 'white',
            'relief': 'flat',
            'width': 15,
            'padx': 15,
            'pady': 10,
            'borderwidth': 0
        }

        save_btn = tk.Button(
            bottom_frame, 
            text="Save", 
            command=self.on_save,
            **button_style,
            bg='#4CAF50',
            activebackground='#45a049'
        )
        save_btn.pack(side=tk.LEFT, padx=10)
        save_btn.bind('<Enter>', lambda e: save_btn.configure(bg='#45a049'))
        save_btn.bind('<Leave>', lambda e: save_btn.configure(bg='#4CAF50'))

        cancel_btn = tk.Button(
            bottom_frame, 
            text="Cancel", 
            command=self.on_cancel,
            **button_style,
            bg='#F44336',
            activebackground='#D32F2F'
        )
        cancel_btn.pack(side=tk.LEFT, padx=10)
        cancel_btn.bind('<Enter>', lambda e: cancel_btn.configure(bg='#D32F2F'))
        cancel_btn.bind('<Leave>', lambda e: cancel_btn.configure(bg='#F44336'))

        exit_btn = tk.Button(
            bottom_frame, 
            text="Exit", 
            command=self.on_exit,
            **button_style,
            bg='#2196F3',
            activebackground='#1976D2'
        )
        exit_btn.pack(side=tk.LEFT, padx=10)
        exit_btn.bind('<Enter>', lambda e: exit_btn.configure(bg='#1976D2'))
        exit_btn.bind('<Leave>', lambda e: exit_btn.configure(bg='#2196F3'))

    def on_day_select(self, day_index):
        for btn in self.day_buttons:
            btn.configure(bg='#2ecc71', fg='white')
        self.day_buttons[day_index-1].configure(bg='#27ae60', fg='white')

        for widget in self.timestamps_frame.winfo_children():
            widget.destroy()

        selected_day_index = day_index - 1
        self.selected_day_index.set(day_index)

        timestamps = self.addDaysController._getTimeStamps()

        added_timestamps = self.addDaysController.ifAdded(self.response, selected_day_index)
        added_timestamps = [x - 1 for x in added_timestamps]

        timestamps_label = tk.Label(
            self.timestamps_frame, 
            text="Select Timestamps",
            font=("Segoe UI", 16, "bold"), 
            bg='#f4f4f8', 
            fg='#2c3e50'
        )
        timestamps_label.pack(pady=(0, 15))

        timestamps_container = tk.Frame(self.timestamps_frame, bg='#f4f4f8')
        timestamps_container.pack(fill='x')

        top_row_frame = tk.Frame(timestamps_container, bg='#f4f4f8')
        bottom_row_frame = tk.Frame(timestamps_container, bg='#f4f4f8')
        top_row_frame.pack(pady=5)
        bottom_row_frame.pack(pady=5)

        half = math.ceil(len(timestamps) / 2)
        self.timestamp_vars = []

        for i, timestamp in enumerate(timestamps):
            var = tk.BooleanVar(value=(i in added_timestamps))
            self.timestamp_vars.append(var)

            btn = tk.Checkbutton(
                top_row_frame if i < half else bottom_row_frame,
                text=str(timestamp),
                variable=var,
                font=("Segoe UI", 12),
                bg='#f4f4f8',
                activebackground='#f4f4f8',
                selectcolor='#2ecc71',
                indicatoron=0,
                width=15,
                borderwidth=1,
                relief='solid',
                compound=tk.CENTER
            )
            btn.pack(side=tk.LEFT, padx=5, pady=5)

    def on_save(self):
        if not self.selected_day_index.get():
            messagebox.showwarning("Warning", "Please select a day first!")
            return

        selected_day_index = self.selected_day_index.get() - 1

        selected_timestamps = [
            i for i, var in enumerate(self.timestamp_vars)
            if var.get()
        ]

        self.addDaysController._saveTimeStamps(selected_timestamps, selected_day_index, self.response)

        messagebox.showinfo("Success", "Timestamps saved successfully!")

    def on_cancel(self):
        self.selected_day_index.set(0)
        for widget in self.timestamps_frame.winfo_children():
            widget.destroy()

        # Reset day button styles
        for btn in self.day_buttons:
            btn.configure(bg='#2ecc71', fg='white')

    def main(self):
        self.window.mainloop()

    def on_exit(self):
        self.addDaysController._teacherHome()

    def close(self):
        self.window.quit()