import tkinter as tk
from tkinter import font, messagebox
from shared_core.View import View
from gui_views.Custom import Custom
import math


class AddDaysView(View):
    def __init__(self, controller, response=None):
        self.addDaysController = controller
        self.response = response
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("Add Days")
        self.window.geometry("1000x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=20, weight="bold")
        title_label = tk.Label(main_frame, text="Add Course Days", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Button style
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        button_style = {
            'font': button_font,
            'width': 25,
            'bg': '#4CAF50',
            'fg': 'white',
            'activebackground': '#45a049',
            'activeforeground': 'white',
            'relief': 'flat',
            'padx': 10,
            'pady': 10
        }

        # Days frame
        days_frame = tk.Frame(main_frame, bg='#f0f0f0')
        days_frame.pack(pady=20)

        # Days label
        days_label = tk.Label(days_frame, text="Select Day", font=("Helvetica", 14), bg='#f0f0f0', fg='#666666')
        days_label.pack(pady=(0, 10))

        # Days buttons
        self.days = self.addDaysController._getDays()
        self.selected_day_index = tk.IntVar()
        self.day_buttons = []

        for day_index, day_name in enumerate(self.days, 1):
            btn = tk.Radiobutton(
                days_frame,
                text=day_name,
                variable=self.selected_day_index,
                value=day_index,
                font=button_font,
                bg='#f0f0f0',
                activebackground='#f0f0f0',
                indicatoron=0,
                width=10,
                command=self.on_day_select
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.day_buttons.append(btn)

        # Timestamps frame
        self.timestamps_frame = tk.Frame(main_frame, bg='#f0f0f0')
        self.timestamps_frame.pack(pady=20)

        # Bottom buttons
        bottom_frame = tk.Frame(main_frame, bg='#f0f0f0')
        bottom_frame.pack(pady=20)

        save_btn = tk.Button(bottom_frame, text="Save", command=self.on_save, **button_style)
        save_btn.pack(side=tk.LEFT, padx=10)
        save_btn.bind('<Enter>', lambda e: save_btn.configure(bg='#45a049'))
        save_btn.bind('<Leave>', lambda e: save_btn.configure(bg='#4CAF50'))

        cancel_btn = tk.Button(bottom_frame, text="Cancel", command=self.on_cancel,
                               **{**button_style, 'bg': '#F44336', 'activebackground': '#D32F2F'})
        cancel_btn.pack(side=tk.LEFT, padx=10)
        cancel_btn.bind('<Enter>', lambda e: cancel_btn.configure(bg='#D32F2F'))
        cancel_btn.bind('<Leave>', lambda e: cancel_btn.configure(bg='#F44336'))

        exit_btn = tk.Button(bottom_frame, text="Exit", 
                             command=self.on_exit,
                             **{**button_style, 'bg': '#2196F3', 'activebackground': '#1976D2'})
        exit_btn.pack(side=tk.LEFT, padx=10)
        exit_btn.bind('<Enter>', lambda e: exit_btn.configure(bg='#1976D2'))
        exit_btn.bind('<Leave>', lambda e: exit_btn.configure(bg='#2196F3'))

    def on_day_select(self):
        # Clear previous timestamps
        for widget in self.timestamps_frame.winfo_children():
            widget.destroy()

        # Get selected day index (already an integer)
        selected_day_index = self.selected_day_index.get() - 1

        # Get timestamps
        timestamps = self.addDaysController._getTimeStamps()

        # Get already added timestamps for this day
        added_timestamps = self.addDaysController.ifAdded(self.response, selected_day_index)
        added_timestamps = [x - 1 for x in added_timestamps]

        # Timestamps label
        timestamps_label = tk.Label(self.timestamps_frame, text="Select Timestamps",
                                    font=("Helvetica", 14), bg='#f0f0f0', fg='#666666')
        timestamps_label.pack(pady=(0, 10))

        # Timestamps buttons
        def create_two_row_layout():
            # Create two frames for two rows
            row1_frame = tk.Frame(self.timestamps_frame, bg='#f0f0f0')
            row1_frame.pack(fill='x', pady=5)
            row2_frame = tk.Frame(self.timestamps_frame, bg='#f0f0f0')
            row2_frame.pack(fill='x', pady=5)

            # Split timestamps into two rows
            half = math.ceil(len(timestamps) / 2)
            self.timestamp_vars = []

            for i, timestamp in enumerate(timestamps):
                var = tk.BooleanVar(value=(i in added_timestamps))
                self.timestamp_vars.append(var)

                btn = tk.Checkbutton(
                    row1_frame if i < half else row2_frame,
                    text=str(timestamp),
                    variable=var,
                    font=("Helvetica", 12),
                    bg='#f0f0f0',
                    activebackground='#f0f0f0'
                )
                btn.pack(side=tk.LEFT, padx=5)
    
        create_two_row_layout()

    def on_save(self):
        if not self.selected_day_index.get():
            messagebox.showwarning("Warning", "Please select a day first!")
            return

        selected_day_index = self.selected_day_index.get() - 1

        # Get selected timestamps
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

    def main(self):
        self.window.mainloop()

    def on_exit(self):
        self.addDaysController._teacherHome()

    def close(self):
        self.window.quit()