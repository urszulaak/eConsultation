import tkinter as tk
from tkinter import messagebox, font, simpledialog, ttk
from shared_core.View import View
from gui_views.Custom import Custom

class CheckBaseConsultView(View):
    def __init__(self, controller, response=None):
        self.controller = controller
        self.window = Custom.get_window()
        Custom.clear_window(self.window)

        self.window.title("eConsultation")
        self.window.geometry("1100x600")
        self.window.configure(bg='#f0f0f0')

        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title_label = tk.Label(main_frame, text="Consultations", font=title_font, bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(0, 20))

        self.tree = ttk.Treeview(main_frame, columns=("Date", "Time", "Assigned", "Topic", "Description"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Assigned", text="Assigned")
        self.tree.heading("Topic", text="Topic")
        self.tree.heading("Description", text="Description")
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', padx=10, pady=(0, 10))

        button_font = font.Font(family="Helvetica", size=10, weight="bold")
        button_style = {
            'font': button_font,
            'bg': '#4CAF50',
            'fg': 'white',
            'activebackground': '#45a049',
            'activeforeground': 'white',
            'relief': 'flat',
            'padx': 10,
            'pady': 5
        }

        # Buttons
        delete_btn = tk.Button(button_frame, text="Delete Consult", command=self.delete_consult, font=button_font, bg='#f44336', fg='white',
                              activebackground='#d32f2f', relief='flat',
                              padx=10, pady=5)
        delete_btn.pack(side='right', padx=5)
        delete_btn.bind('<Enter>', lambda e: delete_btn.configure(bg='#d32f2f'))
        delete_btn.bind('<Leave>', lambda e: delete_btn.configure(bg='#f44336'))

        home_btn = tk.Button(button_frame, text="Home", command=self.go_home, **button_style)
        home_btn.pack(side='right', padx=5)
        home_btn.bind('<Enter>', lambda e: home_btn.configure(bg='#45a049'))
        home_btn.bind('<Leave>', lambda e: home_btn.configure(bg='#4CAF50'))

        self.populate_consultations()

    def populate_consultations(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        consultations = self.controller.getConsult()

        for consult in consultations:
            consult_id, c_date, last_name, first_name, title, description, stamp = consult
            self.tree.insert('', 'end', values=(c_date, stamp, f"{last_name} {first_name}", title, description), tags=(consult_id,))

    def delete_consult(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete Consult", "Please select a consultation to delete.")
            return

        confirm = messagebox.askyesno("Delete Consult", "Are you sure you want to delete this consultation?")
        if confirm:
            consult_id = self.tree.item(selected_item[0], 'tags')[0]
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