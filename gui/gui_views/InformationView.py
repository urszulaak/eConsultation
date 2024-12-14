import tkinter as tk
from tkinter import font
from shared_core.View import View
from gui_views.Custom import Custom

class InformationView(View):
    def __init__(self, controller, response=None):
        self.informationController = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("Application Information")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        # Main frame
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(main_frame, text="Application Information", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 30))

        # Subtitle
        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(main_frame, 
                                  text="Consultation Management Application", 
                                  font=subtitle_font, 
                                  bg='#f0f0f0', 
                                  fg='#666666')
        subtitle_label.pack(pady=(0, 20))

        # Content frame
        content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        content_frame.pack(expand=True, fill='both')

        # Student section
        student_label = tk.Label(content_frame, text="As a Student You Can:", 
                                 font=("Helvetica", 14, "bold"), 
                                 bg='#f0f0f0', 
                                 fg='#333333')
        student_label.pack(anchor='w', padx=20, pady=(0, 10))

        student_features = [
            "Book consultations",
            "Check current consultations"
        ]

        for feature in student_features:
            feature_label = tk.Label(content_frame, 
                                     text=f"• {feature}", 
                                     font=("Helvetica", 12), 
                                     bg='#f0f0f0', 
                                     fg='#666666',
                                     anchor='w')
            feature_label.pack(anchor='w', padx=40)

        # Teacher section
        teacher_label = tk.Label(content_frame, text="As a Teacher You Can:", 
                                 font=("Helvetica", 14, "bold"), 
                                 bg='#f0f0f0', 
                                 fg='#333333')
        teacher_label.pack(anchor='w', padx=20, pady=(20, 10))

        teacher_features = [
            "Add consultations schedule",
            "Check current consultations"
        ]

        for feature in teacher_features:
            feature_label = tk.Label(content_frame, 
                                     text=f"• {feature}", 
                                     font=("Helvetica", 12), 
                                     bg='#f0f0f0', 
                                     fg='#666666',
                                     anchor='w')
            feature_label.pack(anchor='w', padx=40)

        # Navigation buttons frame
        nav_frame = tk.Frame(main_frame, bg='#f0f0f0')
        nav_frame.pack(fill='x', pady=(20, 0))

        # Button style
        button_font = font.Font(family="Helvetica", size=10, weight="bold")
        
        # Home button with red color
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

        # Home button
        home_btn = tk.Button(nav_frame, text="Back to Home", 
                             command=self.go_home,
                             **home_button_style)
        home_btn.pack(side=tk.LEFT, padx=10)

    def go_home(self):
        """Navigate back to the home screen."""
        self.informationController.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()