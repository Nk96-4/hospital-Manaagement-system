import tkinter as tk
from tkinter import messagebox, simpledialog
from Admin import Admin
from Person import Doctor,Patient
patients = [
            Patient('Sara','Smith', 20, '07012345678','B1 234',["Cough", "Fever","Malaria"]),
            Patient('Mike','Jones', 37,'07555551234','L2 2AB',  ["Headache","Fever","Cough"]),
            Patient('Daivd','Smith', 15, '07123456789','C1 ABC', ["Fatigue","Fever"]),
            ]
discharged_patients = []
doctors = [
    Doctor('John', 'Smith', 'Internal Med.'),
    Doctor('Jone', 'Smith', 'Pediatrics'),
    Doctor('Jone', 'Carlos', 'Cardiology'),
]
class HospitalManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.admin = Admin('admin', '123', 'B1 1AB')
        self.doctors = []
        self.patients = []
        self.discharge_patients = []
        self.current_frame = None
        self.login_screen()
        self.names = []
      

    def login_screen(self):
        """Displays the login screen."""
        self.clear_screen()

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Admin Login", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Username:").grid(row=1, column=0, sticky='e')
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1)

        tk.Label(frame, text="Password:").grid(row=2, column=0, sticky='e')
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1)

        def handle_login():
            username = username_entry.get().strip().lower()
            password = password_entry.get()
            if username == self.admin._Admin__username and password == self.admin._Admin__password:
                self.main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!")

        tk.Button(frame, text="Login", command=handle_login).grid(row=3, column=0, columnspan=2, pady=10)

    def main_menu(self):
        """Displays the main menu."""
        self.clear_screen()

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Hospital Management System", font=("Helvetica", 16)).pack(pady=10)

        buttons = [
            ("Doctor Management", self.doctor_management),
            ("Patient Management",self.patient_management),
            ("Discharge Patients", self.discharge_patients),
            ("View Patients", self.view_discharged_patients),
            ("Assign Doctor to a Patient", self.admin_assign_doctor_to_patient),
            ("Update Admin Details", self.update_admin_details),
            ("Group Patients by Family", self.group_patients_by_family),
            ("Load Patient File", self.load_patient_file),
            ("View Reports", self.view_reports),
            ("Quit", self.quit_app)
        ]

        for text, command in buttons:
            tk.Button(frame, text=text, command=command).pack(fill='x', pady=5)

    def doctor_management(self):
     """Doctor management screen."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Doctor Management", font=("Helvetica", 16)).pack(pady=10)
     tk.Button(frame, text="Register Doctor", command=self.add_doctor).pack(fill='x', pady=5)
     tk.Button(frame, text="View Doctors", command=self.view_doctors).pack(fill='x', pady=5)
     tk.Button(frame, text="Update Doctor", command=self.update_doctor).pack(fill='x', pady=5)
     tk.Button(frame, text="Delete Doctor", command=self.delete_doctor).pack(fill='x', pady=5)
     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(fill='x', pady=5)

    def add_doctor(self):
     """Adds a new doctor."""
     first_name = simpledialog.askstring("Input", "Enter doctor's first name:")
     last_name = simpledialog.askstring("Input", "Enter doctor's last name:")
     speciality = simpledialog.askstring("Input", "Enter doctor's speciality:")

     if first_name and last_name and speciality:
        new_doctor = Doctor(first_name, last_name, speciality)
        self.doctors.append(new_doctor)
        messagebox.showinfo("Success", "Doctor added successfully!")
     else:
        messagebox.showerror("Error", "All fields are required!")

    def view_doctors(self):
     """Displays the list of doctors in a scrollable frame."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True, fill="both")
     tk.Label(frame, text="List of Doctors", font=("Helvetica", 16)).pack(pady=10)
     for doctor in doctors:
      print(doctor.get_first_name(), doctor.get_surname(), doctor.get_speciality())
     canvas = tk.Canvas(frame)
     scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
     scrollable_frame = tk.Frame(canvas)

     scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
     )
     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
     canvas.configure(yscrollcommand=scrollbar.set)
     canvas.pack(side="left", fill="both", expand=True)
     scrollbar.pack(side="right", fill="y")

     if self.doctors:
        for index, doctor in enumerate(self.doctors, start=1):
            tk.Label(
                scrollable_frame,
                text=f"{index}. {doctor.full_name()} - {doctor.get_speciality()}",
                anchor="w"
            ).pack(fill="x", pady=2)
     else:
        tk.Label(scrollable_frame, text="No doctors registered yet.", anchor="w").pack()

     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def update_doctor(self):
     """Displays the list of doctors and allows updating their details."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Update Doctor Information", font=("Helvetica", 16)).pack(pady=10)
     canvas = tk.Canvas(frame)
     scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
     scrollable_frame = tk.Frame(canvas)

     scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
     )
     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
     canvas.configure(yscrollcommand=scrollbar.set)
     canvas.pack(side="left", fill="both", expand=True)
     scrollbar.pack(side="right", fill="y")

     if self.doctors:
        for index, doctor in enumerate(self.doctors, start=1):
            tk.Label(
                scrollable_frame,
                text=f"{index}. {doctor.full_name()} - {doctor.get_speciality()}",
                anchor="w"
            ).grid(row=index, column=0, sticky="w", padx=5, pady=2)

            update_button = tk.Button(
                scrollable_frame,
                text="Update",
                command=lambda d=doctor: self.update_doctor_dialog(d)
            )
            update_button.grid(row=index, column=1, padx=5, pady=2)
     else:
        tk.Label(scrollable_frame, text="No doctors registered yet.", anchor="w").pack()

     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)
    def update_doctor_dialog(self, doctor):
     """Opens a dialog to update a doctor's details."""
     update_window = tk.Toplevel(self.root)
     update_window.title("Update Doctor Details")

     tk.Label(update_window, text="Update Doctor Details", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

     tk.Label(update_window, text="First Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
     first_name_entry =simpledialog.askstring("Input", "Enter doctor's first name:")
     
     tk.Label(update_window, text="Last Name:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
     last_name_entry =simpledialog.askstring("Input", "Enter doctor's last name:")
     tk.Label(update_window, text="Speciality:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
     speciality_entry = simpledialog.askstring("Input", "Enter doctor's speciality:")
     messagebox.showinfo("Success", "Doctor details updated successfully!")
     update_window.destroy()

     def save_changes():
      doctor.first_name = first_name_entry.get()
      doctor.last_name = last_name_entry.get()
      doctor.speciality = speciality_entry.get()
      messagebox.showinfo("Success", "Doctor details updated successfully!")
      update_window.destroy()

      tk.Button(update_window, text="Save Changes", command=save_changes).grid(row=4, column=0, columnspan=2, pady=10)
      tk.Button(update_window, text="Cancel", command=update_window.destroy).grid(row=5, column=0, columnspan=2, pady=5)
    def delete_doctor(self):
     """Displays the list of doctors and allows deletion."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Delete Doctor", font=("Helvetica", 16)).pack(pady=10)
     canvas = tk.Canvas(frame)
     scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
     scrollable_frame = tk.Frame(canvas)

     scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
     )
     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
     canvas.configure(yscrollcommand=scrollbar.set)
     canvas.pack(side="left", fill="both", expand=True)
     scrollbar.pack(side="right", fill="y")

     if self.doctors:
        for index, doctor in enumerate(self.doctors, start=1):
            tk.Label(
                scrollable_frame,
                text=f"{index}. {doctor.full_name()} - {doctor.get_speciality()}",
                anchor="w"
            ).grid(row=index, column=0, sticky="w", padx=5, pady=2)

            delete_button = tk.Button(
                scrollable_frame,
                text="Delete",
                command=lambda d=doctor: self.confirm_delete_doctor(d)
            )
            delete_button.grid(row=index, column=1, padx=5, pady=2)
     else:
        tk.Label(scrollable_frame, text="No doctors registered yet.", anchor="w").pack()

     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def confirm_delete_doctor(self, doctor):
     """Confirms the deletion of a doctor."""
     confirm = messagebox.askyesno(
        "Confirm Deletion",
        f"Are you sure you want to delete {doctor.full_name()}?"
     )
     if confirm:
        self.doctors.remove(doctor)
        messagebox.showinfo("Success", "Doctor deleted successfully!")
        self.delete_doctor()
        
      
        #patient management
    def patient_management(self):
     """Patient management screen."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Patient Management", font=("Helvetica", 16)).pack(pady=10)
    
    # Add options for managing patients
     tk.Button(frame, text="Add Patient", command=self.add_patient).pack(fill='x', pady=5)
     tk.Button(frame, text="Assign Doctor to Patient", command=self.assign_doctor_to_patient).pack(fill='x', pady=5)
     tk.Button(frame, text="View Assigned Doctors", command=self.view_assigned_doctors).pack(fill='x', pady=5)
     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(fill='x', pady=5)

    def add_patient(self):
     first_name = simpledialog.askstring("Input", "Enter patient's first name:")
     last_name = simpledialog.askstring("Input", "Enter patient's last name:")
     age = simpledialog.askstring("Input", "Enter patient's age:")
     mobile = simpledialog.askstring("Input", "Enter patient's mobile:")
     postcode = simpledialog.askstring("Input", "Enter patient's postcode:")
     symptom = simpledialog.askstring("Input", "Enter patient's symptoms:")

     if first_name and last_name and age and mobile and postcode and symptom:
        new_patient = Patient(first_name, last_name, age, mobile, postcode, symptom)
        self.patients.append(new_patient)
        messagebox.showinfo("Success", "Patient added successfully!")
     else:
        messagebox.showerror("Error", "All fields are required!")
    def assign_doctor_to_patient(self):
     """Assign a doctor to a patient."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Assign Doctor to Patient", font=("Helvetica", 16)).pack(pady=10)
    
    # List doctors
     tk.Label(frame, text="Select Doctor").pack(pady=5)
     doctor_listbox = tk.Listbox(frame)
     for doctor in self.doctors:
        doctor_listbox.insert(tk.END, f"{doctor.full_name()} - {doctor.get_speciality()}")
     doctor_listbox.pack(pady=10)

    # List patients
     tk.Label(frame, text="Select Patient").pack(pady=5)
     patient_listbox = tk.Listbox(frame)
     for patient in self.patients:
        patient_listbox.insert(tk.END, f"{patient.get_first_name()} {patient.get_surname()}")
     patient_listbox.pack(pady=10)

     def assign_doctor():
        doctor_index = doctor_listbox.curselection()
        patient_index = patient_listbox.curselection()
        if doctor_index and patient_index:
            doctor = self.doctors[doctor_listbox.curselection()[0]]
            patient = self.patients[patient_listbox.curselection()[0]]
            patient.assign_doctor(doctor)
            doctor.add_patient(patient)
            messagebox.showinfo("Success", f"Doctor {doctor.full_name()} assigned to patient {patient.get_first_name()} {patient.get_surname()}")
        else:
            messagebox.showerror("Error", "Please select both a doctor and a patient.")
    
     tk.Button(frame, text="Assign Doctor", command=assign_doctor).pack(pady=10)
     tk.Button(frame, text="Back to Patient Management", command=self.patient_management).pack(pady=5)
    def view_assigned_doctors(self):
     """View assigned doctor for each patient."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Assigned Doctors for Patients", font=("Helvetica", 16)).pack(pady=10)
    
     if self.patients:
        for patient in self.patients:
         doctor_info = print("Not assigned") if patient.assigned_doctor is None else f"Dr. {patient.assigned_doctor.full_name()} - {patient.assigned_doctor.get_speciality()}"
         tk.Label(frame, text=f"{patient.get_first_name()} {patient.get_surname()}: {doctor_info}").pack(pady=5)
     else:
        tk.Label(frame, text="No patients added yet.").pack(pady=5)
        tk.Button(frame, text="Back to Patient Management", command=self.patient_management).pack(pady=5)

    def discharge_patients(self):
     """Allows selecting and discharging patients."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Discharge Patients", font=("Helvetica", 16)).pack(pady=10)
     canvas = tk.Canvas(frame)
     scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
     scrollable_frame = tk.Frame(canvas)

     scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
     )
     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
     canvas.configure(yscrollcommand=scrollbar.set)
     canvas.pack(side="left", fill="both", expand=True)
     scrollbar.pack(side="right", fill="y")

     if patients:
        for index, patient in enumerate(patients, start=1):
            tk.Label(
                scrollable_frame,
                text=f"{index}. {patient.full_name()} - {patient.condition}",
                anchor="w"
            ).grid(row=index, column=0, sticky="w", padx=5, pady=2)

            discharge_button = tk.Button(
                scrollable_frame,
                text="Discharge",
                command=lambda p=patient: self.confirm_discharge(p, patients, discharged_patients)
            )
            discharge_button.grid(row=index, column=1, padx=5, pady=2)
     else:
        tk.Label(scrollable_frame, text="No patients admitted currently.", anchor="w").pack()

        tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def view_discharged_patients(self):
        self.clear_screen()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        tk.Label(frame, text="Patient list", font=("Helvetica", 16)).pack(pady=10)
        for patient in patients:
         print(patient.get_first_name(), patient.get_surname(), patient.get_age(), patient.get_mobile(), patient.get_postcode(), patient.get_symptoms())
        tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)
        
    def admin_assign_doctor_to_patient(self):
        assign_window = tk.Toplevel(self.root)
        assign_window.title("Assign Doctor to Patient")

        tk.Label(assign_window, text="----- Assign -----").pack(pady=5)

        tk.Label(assign_window, text="----- Patients -----").pack(pady=5)
        tk.Label(assign_window, text="Select a patient:").pack()

        patient_listbox = tk.Listbox(assign_window)
        for patient in self.patients:
            patient_listbox.insert(tk.END, f'{patient.id} | {patient.full_name} | {patient.age}')
        patient_listbox.pack(pady=5)

        def on_patient_select(event):
            patient_index = patient_listbox.curselection()[0]
            selected_patient = self.patients[patient_index]
            tk.Label(assign_window, text="----- Doctors Select -----").pack(pady=10)
            tk.Label(assign_window, text="Select a doctor:").pack()
            doctor_listbox = tk.Listbox(assign_window)
            for doctor in self.doctors:
                doctor_listbox.insert(tk.END, f'{doctor.id} | {doctor.full_name} | {doctor.specialty}')
            doctor_listbox.pack(pady=5)

            def on_doctor_select(event):
                doctor_index = doctor_listbox.curselection()[0]
                selected_doctor = self.doctors[doctor_index]
                selected_patient.link(selected_doctor.full_name)
                selected_doctor.add_patient(selected_patient)
                messagebox.showinfo("Success", f"Patient {selected_patient.full_name} assigned to Dr. {selected_doctor.full_name}.")
            doctor_listbox.bind("<<ListboxSelect>>", on_doctor_select)
            patient_listbox.bind("<<ListboxSelect>>", on_patient_select)
            
            
     #update admin details
    def update_admin_details(self):
     """Displays the admin details update screen."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Update Admin Details", font=("Helvetica", 16)).pack(pady=10)

    # Create entry fields for the name and password
     tk.Label(frame, text="Admin Name:").pack(padx=20, pady=10)
     self.name_entry = tk.Entry(frame)
     self.name_entry.pack(padx=20, pady=10)

     tk.Label(frame, text="Admin Password:").pack(padx=20, pady=10)
     self.password_entry = tk.Entry(frame, show="*")  # Mask the password input
     self.password_entry.pack(padx=20, pady=10)

     # Create a button to save changes
     tk.Button(frame, text="Update Details", command=self.save_admin_details).pack(pady=10)
     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def save_admin_details(self):
     """Saves the updated admin details."""
     new_name = self.name_entry.get().strip()
     new_password = self.password_entry.get().strip()

     if new_name and new_password:
        self.admin._Admin__username = new_name  
        self.admin._Admin__password = new_password
        messagebox.showinfo("Success", "Admin details updated successfully!")
        self.main_menu()
     else:
        messagebox.showerror("Error", "Both name and password must be provided.")

    def group_patients_by_family(self):
     """Groups patients by their surname."""
     if not self.patients:
        messagebox.showwarning("No Patients", "There are no patients to group.")
        return
    
     surname_groups = {}
     for patient in self.patients:
        surname = patient.get_surname()  
        if surname not in surname_groups:
            surname_groups[surname] = []
        surname_groups[surname].append(patient)

     self.result_listbox.delete(0, tk.END)

     for surname, patients in surname_groups.items():
        group_str = f"Surname: {surname}"
        self.result_listbox.insert(tk.END, group_str)
        for patient in patients:
            self.result_listbox.insert(tk.END, f"  {patient.first_name} {patient.surname}, Age: {patient.age}")


    def load_patient_file(self):
     try:
        file_path = simpledialog.askstring("File Path", "Enter the file path for patient data:")
        if not file_path:
            return

        self.patients = self.admin.load_patients_from_file(file_path)
        messagebox.showinfo("Load Success", f"Loaded {len(self.patients)} patients from {file_path}.")
     except Exception as e:
        messagebox.showerror("Load Error", f"An error occurred: {e}")

    def view_reports(self):
     """Displays the hospital reports."""
     self.clear_screen()
     frame = tk.Frame(self.root, padx=20, pady=20)
     frame.pack(expand=True)

     tk.Label(frame, text="Hospital Reports", font=("Helvetica", 16)).pack(pady=10)

     report_text = f"""
     Total Number of Doctors: {len(self.doctors)}
     Total Number of Patients: {len(self.patients)}
     Total Number of Discharged Patients: {len(self.discharge_patients)}
     """
     report_label = tk.Label(frame, text=report_text, justify="left")
     report_label.pack(pady=10)

     tk.Button(frame, text="Back to Main Menu", command=self.main_menu).pack(pady=10)
    
    def quit_app(self):
        """Exits the application."""
        self.root.quit()
        for widget in self.root.winfo_children():
            widget.destroy()
    def clear_screen(self):
        """Clears the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystemGUI(root)
    root.mainloop()
