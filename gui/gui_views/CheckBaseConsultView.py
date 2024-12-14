import tkinter as tk
from tkinter import messagebox, font, ttk
from shared_core.View import View
from gui_views.Custom import Custom

class CheckBaseConsultView(View):
    def __init__(self, controller, response=None):
        self.controller = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        # Color and style settings
        COLORS = {
            'background': '#f5f5f5',
            'primary': '#4CAF50',
            'secondary': '#3B963E',
            'text_dark': '#333333',
            'text_light': '#FFFFFF',
            'button_active': '#45a049',
            'button_hover': '#388e3c',
            'button_delete': '#e74c3c',
            'button_delete_hover': '#c0392b'
        }

        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg=COLORS['background'])

        main_frame = tk.Frame(self.window, bg=COLORS['background'])
        main_frame.pack(expand=True, fill='both', padx=30, pady=30)

        title_font = font.Font(family="Segoe UI", size=max(24, int(self.window.winfo_screenwidth() * 0.02)), weight="bold")
        title_label = tk.Label(main_frame, text="Consultations", font=title_font, bg=COLORS['primary'], fg=COLORS['text_light'], anchor='center')
        title_label.pack(fill='x', pady=(0, 30))

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("Custom.Treeview", 
            background="#ffffff", 
            foreground="#2c3e50",
            rowheight=35,
            fieldbackground="#ffffff"
        )
        style.configure("Custom.Treeview.Heading", 
            background=COLORS['primary'], 
            foreground="white", 
            font=('Segoe UI', 10, 'bold')
        )
        style.map("Custom.Treeview", 
            background=[('selected', COLORS['secondary'])],  
            foreground=[('selected', 'white')]
        )

        self.sort_column = "Date"
        self.sort_order = False

        self.tree = ttk.Treeview(main_frame, 
            columns=("Date", "Time", "Assigned", "Topic", "Description"), 
            show="headings", 
            style="Custom.Treeview"
        )

        self.tree.column("Date", width=100, anchor='center')
        self.tree.column("Time", width=80, anchor='center')
        self.tree.column("Assigned", width=150, anchor='center')
        self.tree.column("Topic", width=200, anchor='center')
        self.tree.column("Description", width=350, anchor='w')

        self.tree.heading("Date", text="Date", anchor='center', command=lambda: self.sort_treeview("Date"))
        self.tree.heading("Time", text="Time", anchor='center', command=lambda: self.sort_treeview("Time"))
        self.tree.heading("Assigned", text="Assigned", anchor='center', command=lambda: self.sort_treeview("Assigned"))
        self.tree.heading("Topic", text="Topic", anchor='center', command=lambda: self.sort_treeview("Topic"))
        self.tree.heading("Description", text="Description", anchor='center', command=lambda: self.sort_treeview("Description"))

        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        button_frame = tk.Frame(main_frame, bg=COLORS['background'])
        button_frame.pack(fill='x', padx=10, pady=(10, 0))

        button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        
        delete_btn = tk.Button(
            button_frame, 
            text="Delete Consultation", 
            command=self.delete_consult, 
            font=button_font, 
            bg=COLORS['button_delete'], 
            fg=COLORS['text_light'],
            activebackground=COLORS['button_delete_hover'], 
            relief='flat',
            padx=12, 
            pady=6,
            borderwidth=0
        )
        delete_btn.pack(side='right', padx=5)
        delete_btn.bind('<Enter>', lambda e: delete_btn.configure(bg=COLORS['button_delete_hover']))
        delete_btn.bind('<Leave>', lambda e: delete_btn.configure(bg=COLORS['button_delete']))

        home_btn = tk.Button(
            button_frame, 
            text="Home", 
            command=self.go_home, 
            font=button_font, 
            bg=COLORS['primary'], 
            fg=COLORS['text_light'],
            activebackground=COLORS['button_active'], 
            relief='flat',
            padx=12, 
            pady=6,
            borderwidth=0
        )
        home_btn.pack(side='right', padx=5)
        home_btn.bind('<Enter>', lambda e: home_btn.configure(bg=COLORS['button_active']))
        home_btn.bind('<Leave>', lambda e: home_btn.configure(bg=COLORS['primary']))

        self.populate_consultations()

    def populate_consultations(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        consultations = self.controller.getConsult()

        for idx, consult in enumerate(consultations):
            consult_id, c_date, last_name, first_name, title, description, stamp = consult
            tags = ('oddrow',) if idx % 2 == 0 else ('evenrow',)
            self.tree.insert('', 'end', 
                values=(c_date, stamp, f"{last_name} {first_name}", title, description), 
                tags=tags + (consult_id,)
            )
        
        self.tree.tag_configure('oddrow', background='#f8f9fa')
        self.tree.tag_configure('evenrow', background='#ffffff')

    def sort_treeview(self, col):
        if self.sort_column == col:
            self.sort_order = not self.sort_order
        else:
            self.sort_column = col
            self.sort_order = False

        consultations = self.controller.getConsult()

        def get_sort_key(consult):
            column_index = {"Date": 0, "Time": 1, "Assigned": 2, "Topic": 3, "Description": 4}[col]
            return consult[column_index]

        consultations.sort(key=get_sort_key, reverse=self.sort_order)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for idx, consult in enumerate(consultations):
            consult_id, c_date, last_name, first_name, title, description, stamp = consult
            tags = ('oddrow',) if idx % 2 == 0 else ('evenrow',)
            self.tree.insert('', 'end', 
                values=(c_date, stamp, f"{last_name} {first_name}", title, description), 
                tags=tags + (consult_id,)
            )

        self.tree.tag_configure('oddrow', background='#f8f9fa')
        self.tree.tag_configure('evenrow', background='#ffffff')

    def delete_consult(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete Consult", "Please select a consultation to delete.")
            return

        confirm = messagebox.askyesno("Delete Consult", "Are you sure you want to delete this consultation?")
        if confirm:
            consult_id = self.tree.item(selected_item[0], 'tags')[-1]
            self.controller.delete_consult(consult_id)
            self.populate_consultations()

    def go_home(self):
        self.window.quit()
        self.controller.home()

    def main(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()

class CheckConsultView(CheckBaseConsultView):
    pass

class CheckUConsultView(CheckBaseConsultView):
    pass
