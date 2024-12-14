import tkinter as tk
from tkinter import font
from shared_core.View import View
from gui_views.Custom import Custom

class InformationView(View):
    def __init__(self, controller, response=None):
        self.informationController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        COLORS = {
        'background': '#F5F5F5',
        'primary': '#4CAF50',
        'secondary': '#3B963E',
        'text_dark': '#333333',
        'text_light': '#FFFFFF'
        }

        self.window.title("Application Information")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Application Information", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(main_frame, text="Consultation Management Application", font=subtitle_font, bg='#f0f0f0', fg='#666666')
        subtitle_label.pack(pady=(0, 20))

        content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        content_frame.pack(expand=True, fill='both')

        left_frame = tk.Frame(content_frame, bg='#f0f0f0', width=550)
        left_frame.pack(side=tk.LEFT, expand=True, fill='both', padx=10)

        student_label = tk.Label(left_frame, text="As a Student You Can:", font=("Helvetica", 14, "bold"), bg='#f0f0f0', fg='#333333')
        student_label.pack(anchor='center', pady=(10, 10))

        student_features = [
            "Book consultations",
            "Check current consultations"
        ]

        for feature in student_features:
            feature_label = tk.Label(left_frame, text=f"• {feature}", font=("Helvetica", 12), bg='#f0f0f0', fg='#666666', anchor='center')
            feature_label.pack(anchor='center', pady=5)

        right_frame = tk.Frame(content_frame, bg='#f0f0f0', width=550)
        right_frame.pack(side=tk.LEFT, expand=True, fill='both', padx=10)

        teacher_label = tk.Label(right_frame, text="As a Teacher You Can:", font=("Helvetica", 14, "bold"), bg='#f0f0f0', fg='#333333')
        teacher_label.pack(anchor='center', pady=(10, 10))  # Adjusted padding to match student section

        teacher_features = [
            "Add consultations schedule",
            "Check current consultations"
        ]

        for feature in teacher_features:
            feature_label = tk.Label(right_frame, text=f"• {feature}", font=("Helvetica", 12), bg='#f0f0f0', fg='#666666',anchor='center')
            feature_label.pack(anchor='center', pady=5)

        nav_frame = tk.Frame(main_frame, bg='#f0f0f0')
        nav_frame.pack(fill='x', pady=(20, 0))

        button_font = font.Font(family="Helvetica", size=10, weight="bold")

        home_button_style = {
            'font': button_font,
            'width': 15,
            'bg': '#f44336', 
            'fg': 'white',
            'activebackground': '#d32f2f',
            'activeforeground': 'white',
            'relief': 'flat',
            'padx': 10,
            'pady': 5
        }

        home_btn = tk.Button(nav_frame, text="Back to Home", command=self.go_home, **home_button_style)
        home_btn.pack(side=tk.TOP, pady=(10, 0))

    def go_home(self):
        self.informationController.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
