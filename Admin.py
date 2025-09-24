
from Person import Doctor,Patient
class Admin:


    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
       

        self.__username = username
        self.__password = password
        self.__address =  address
       

        
    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        
        print("----Welcome to our Hospital system,please login first------")
        
        username = input('Please enter the username: ').strip().lower()
        password = input('Please enter the password: ')

        print(username == self.__username)
        print(password == self.__password)
        
        if (username == self.__username) and (password == self.__password):
            return True
        else:
            return False
           
    def find_index(self,index,doctors):
        
        """check that the doctor id exists  """        
        if index in range(0,len(doctors)):
            return True
        else:
            return False
            
    def get_doctor_details(self) :
       
        first_name=input("Enter the first name:")
        surname=input("Enter the surname name:")
        speciality=input("Enter the speciality:")
        return first_name, surname, speciality

    def doctor_management(self, doctors,patients):
     while True:
        print("-----Doctor Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        print(' 5 - Assign patient')
        print(' 6 - View assigned patients')
        print(' 7 - Exit')
        op = input("****\nSelect an option: ")
        if op == '1':
            print("-----Register-----")
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
            if any(first_name == doctor.get_first_name() and surname == doctor.get_surname() for doctor in doctors):
                print('Name already exists.')
            else:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print("Doctor registered successfully.")

        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        elif op == '3':
            while True:
                print("-----Update Doctor's Details-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        break
                    else:
                        print("Doctor not found.")
                except ValueError:
                    print('The ID entered is incorrect.')

            print('Choose the field to be updated:')
            print(' 1 - First Name')
            print(' 2 - Surname')
            print(' 3 - Speciality')
            try:
                op = int(input("Select an option (1-3): "))
                if op == 1:
                    new_first_name = input("Enter the new first name: ")
                    if new_first_name:
                        doctors[index].set_first_name(new_first_name)
                        print("First name updated successfully.")
                    else:
                        print("First name cannot be empty.")

                elif op == 2:
                    new_surname = input("Enter the new surname: ")
                    if new_surname:
                        doctors[index].set_surname(new_surname)
                        print("Surname updated successfully.")
                    else:
                        print("Surname cannot be empty.")

                elif op == 3:
                    new_speciality = input("Enter the new speciality: ")
                    if new_speciality:
                        doctors[index].set_speciality(new_speciality)
                        print("Speciality updated successfully.")
                    else:
                        print("Speciality cannot be empty.")

                else:
                    print("Invalid choice. Please select a valid option.")

            except ValueError:
                print('The ID entered is incorrect.')

        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            try:
                doctor_index = int(doctor_index) - 1
                if self.find_index(doctor_index, doctors):
                    del doctors[doctor_index]
                    print("Doctor deleted successfully.")
                else:
                    print("The ID entered is incorrect.")
            except ValueError:
                print("Invalid ID entered. Check your spelling!")
        elif op == '5':  # Assign patients to doctor
         print("\n--- Assign Doctor to patient ---")
          # List available doctors
         print("\nAvailable Doctors:")
         for i, doctor in enumerate(doctors, start=1):
          print(f"{i}. {doctor.full_name()} ({doctor.get_speciality()})")
    
         try:
          doctor_index = int(input("\nSelect a doctor by ID: ")) - 1
          if doctor_index in range(len(doctors)):
            selected_doctor = doctors[doctor_index]
            
            # List unassigned patients
            unassigned_patients = [patient for patient in patients if patient.assigned_doctor is None]
            if not unassigned_patients:
                print("No unassigned patients available.")
                return
            
            print("\nAvailable Patients:")
            for i, patient in enumerate(unassigned_patients, start=1):
                print(f"{i}. {patient}")
            
            try:
                patient_index = int(input("\nSelect a patient by ID: ")) - 1
                if patient_index in range(len(unassigned_patients)):
                    selected_patient = unassigned_patients[patient_index]
                    selected_patient.assign_doctor(selected_doctor)  # Assign the doctor
                    selected_doctor.add_patient(selected_patient)  # Add the patient to the doctor's list
                    print(f"Dr. {selected_doctor.full_name()} successfully assigned to Patient {selected_patient} .")
                
            except ValueError:
                    print("Invalid input. Please enter a valid patient ID.")
            else:
             print("Invalid doctor ID.")
         except ValueError:
             print("Invalid input. Please enter a valid doctor ID.")

         
        elif op == '6':  # View assigned patients
          print("\n--- View Assigned Patients ---")
          for i, doctor in enumerate(doctors, start=1):
           print(f"{i}. {doctor.full_name()} ({doctor.get_speciality()})")
    
          try:
            doctor_index = int(input("\nSelect a doctor by ID to view their patients: ")) - 1
            if doctor_index in range(len(doctors)):
             doctors[doctor_index].view_assigned_patients()
            else:
             print("Invalid doctor ID.")
          except ValueError:
           print("Invalid input. Please enter a valid doctor ID.")


        # Exit
        elif op == '7':
            print("Exiting Doctor Management...")
            break

        # Invalid input
        else:
            print("Invalid choice. Please select a valid option.")


    

    def view_patient(self, patients):
       
        print("-----View Patients-----")
        print('ID |     Full Name   | Age |    Mobile     | Postcode  | Symptoms')
        self.view(patients)
        
    def patient_management(self,doctors,patients):
     while True:
        print("\n-----Patient Management-----")
        print('Choose the operation:')
        print(' 1 - Assign Patient to Doctor')
        print(' 2 - Add Patientt')
        print(' 3 - View Assigned Doctors for Patients')
        print(' 4 - Exit')
        op = input("****\nSelect an option: ")

        if op == '1':
            print("\n--- Assign Patients to a Doctor ---")
            
            # List available doctors
            print("\nAvailable Doctors:")
            for i, doctor in enumerate(doctors, start=1):
                print(f"{i}. {doctor.full_name()} ({doctor.get_speciality()})")
            
            try:
                doctor_index = int(input("\nSelect a doctor by ID: ")) - 1
                if doctor_index in range(len(doctors)):
                    selected_doctor = doctors[doctor_index]

                    # List unassigned patients
                    unassigned_patients = [patient for patient in patients if patient.assigned_doctor is None]
                    if not unassigned_patients:
                        print("No unassigned patients available.")
                        return
                    
                    print("\nAvailable Patients:")
                    for i, patient in enumerate(unassigned_patients, start=1):
                        print(f"{i}. {patient}")

                    try:
                        patient_index = int(input("\nSelect a patient by ID: ")) - 1
                        if patient_index in range(len(unassigned_patients)):
                            selected_patient = unassigned_patients[patient_index]
                            selected_patient.assign_doctor(selected_doctor)
                            selected_doctor.add_patient(selected_patient)
                            print(f"Patient {selected_patient} successfully assigned to Dr. {selected_doctor.full_name()}.")
                        else:
                            print("Invalid patient ID.")
                    except ValueError:
                        print("Invalid input. Please enter a valid patient ID.")
                else:
                    print("Invalid doctor ID.")
            except ValueError:
                print("Invalid input. Please enter a valid doctor ID.")


        elif op == '2':
           """Adds a new patient to the system."""
           print("----- Add New Patient -----")
          
           first_name = input("Enter patient's first name: ").strip()
           surname = input("Enter patient's surname: ").strip()
           age = input("Enter patient's age: ").strip()
           mobile = input("Enter patient's mobile number: ").strip()
           postcode = input("Enter patient's postcode: ").strip()
           symptoms = input("Enter patient's symptoms (comma separated): ").strip()

           # Convert symptoms string into a list
           symptoms_list = symptoms.split(",") if symptoms else []

          # Validate that all necessary fields are entered
           if first_name and surname and age.isdigit() and mobile and postcode:
              # Create a new Patient object
              new_patient = Patient(first_name, surname, int(age), mobile, postcode, symptoms_list)
              
              # Add the new patient to the list of patients
              patients.append(new_patient)
              print(f"Patient {first_name} {surname} added successfully!")
           else:
              print("Invalid input. Please make sure all fields are filled correctly.")

        elif op == '3':
         """View the doctor assigned to a specific patient."""
         print("\n--- View Assigned Doctor ---")
         for i, patient in enumerate(patients, start=1):
          print(f"{i}. {patient.get_first_name()} {patient.get_surname()} (Age: {patient.get_age()})")
         try:
        
          patient_index = int(input("\nSelect a patient by ID to view their assigned doctor: ")) - 1
        
     
          if patient_index in range(len(patients)):
            selected_patient = patients[patient_index]
            
            # Display the assigned doctor
            if selected_patient.assigned_doctor:
                assigned_doctor = selected_patient.assigned_doctor
                print(f"\nAssigned Doctor for {selected_patient.get_first_name()} {selected_patient.get_surname()}:")
                print(f"- Dr. {assigned_doctor.full_name()} ({assigned_doctor.get_speciality()})")
            else:
                print("No doctor has been assigned to this patient yet.")
          else:
            print("Invalid patient ID.")
         except ValueError:
          print("Invalid input. Please enter a valid patient ID.")


        elif op == '4':
            print("Exiting Patient Management...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

    
    
    def assign_doctor_to_patient(self, patients, doctors):
        
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |     Full Name   | Age |    Mobile     | Postcode | Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) -1

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return 

        except ValueError: 
            print('The id entered is incorrect')
            return 

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) -1
            if self.find_index(doctor_index,doctors)!=False:
             patients[patient_index].assign_doctor (doctors[doctor_index].full_name())
             doctors[doctor_index].add_patient(patients[patient_index])
             print('The patient is now assign to the doctor.')
            
             print("\n----- Assigned Doctor and Patient -----")
             print(f"Patient: {patients[patient_index].full_name()}")
             print(f"Assigned Doctor: {doctors[doctor_index].full_name()}")
            else:
                print('The id entered was not found.')
        except ValueError: 
            print('The id entered is incorrect')

            


    def discharge(self, patients, discharged_patients):
      """
      Allow the admin to discharge a patient when treatment is done.
      Args:
        patients (list<Patients>): the list of all the active patients
        discharged_patients (list<Patients>): the list of all the non-active patients
      """
      while True:
        print("----- Discharge Patient -----")
        print("Current Active Patients:")
        self.view(patients)

        choice = input("Do you want to discharge a patient? (Y/N): ").strip().upper()

        if choice == 'Y' or choice == 'YES':
            patient_id = input("Enter the patient ID to discharge: ").strip()
            try:
                patient_index = int(patient_id) - 1  
                if self.find_index(patient_index, patients):
                    discharged_patients.append(patients.pop(patient_index))
                    print("Patient discharged successfully.")
                else:
                    print("Invalid Patient ID. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")
        elif choice == 'N' or choice == 'NO':
            print("Exiting discharge process.")
            break
        else:
            print("Invalid choice. Please answer with 'Y' or 'N'.")

    def add_patient(self, patients):
     """Adds a new patient to the system."""
     print("----- Add New Patient -----")
    
     first_name = input("Enter patient's first name: ").strip()
     surname = input("Enter patient's surname: ").strip()
     age = input("Enter patient's age: ").strip()
     mobile = input("Enter patient's mobile number: ").strip()
     postcode = input("Enter patient's postcode: ").strip()
     symptoms = input("Enter patient's symptoms (comma separated): ").strip()

     # Convert symptoms string into a list
     symptoms_list = symptoms.split(",") if symptoms else []

    # Validate that all necessary fields are entered
     if first_name and surname and age.isdigit() and mobile and postcode:
        # Create a new Patient object
        new_patient = Patient(first_name, surname, int(age), mobile, postcode, symptoms_list)
        
        # Add the new patient to the list of patients
        patients.append(new_patient)
        print(f"Patient {first_name} {surname} added successfully!")
     else:
        print("Invalid input. Please make sure all fields are filled correctly.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)


    def update_details(self):
     while True:
        print("\n----- Update Details -----")
        print("1. Update Username")
        print("2. Update Password")
        print("3. Update Address")
        print("4. Exit")
        try:
            op = int(input("Select an option (1-4): ").strip())
            if op == 1:
                new_username = input("Enter the new username: ").strip()
                if new_username:
                    self.__username = new_username
                    print("Username updated successfully.")
                else:
                    print("Username cannot be empty.")
            elif op == 2:
                while True:
                    password = input("Enter the new password: ").strip()
                    confirm_password = input("Re-enter the new password: ").strip()
                    if password == confirm_password:
                        self.__password = password
                        print("Password updated successfully.")
                        break
                    else:
                        print("Passwords do not match. Please try again.")
            elif op == 3:
                new_address = input("Enter the new address: ").strip()
                if new_address:
                    self.__address = new_address
                    print("Address updated successfully.")
                else:
                    print("Address cannot be empty.")
            elif op == 4:
                print("Exiting update menu.")
                break
            else: 
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            

    def group_patients_by_surname(self, patients):
        """Groups patients by surname."""
        surname_groups = {}
        for patient in patients:
            surname = patient.get_surname()  
            if surname not in surname_groups:
                surname_groups[surname] = []
            surname_groups[surname].append(patient)
        return surname_groups

  
    def save_patients_to_file(patients, file_name="patients_record.txt"):
     """Save patient records to a text file."""
     with open(file_name, 'w') as file:
        for patient in patients:
            file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.__age},"
                           f"{patient.__mobile},{patient.__postcode},{';'.join(patient.__symptoms)}\n")
        print(f"Patient records saved to {file_name}.")


    
    def load_patients_from_file(self, file_name="patients_record.txt"):
        """Load patient records from a text file."""
        patient_list = []
        patients = [
                    Patient('Sara','Smith', 20, '07012345678','B1 234',["Cough", "Fever","Malaria"]),
                    Patient('Mike','Jones', 37,'07555551234','L2 2AB',  ["Headache","Fever","Cough"]),
                    Patient('Daivd','Smith', 15, '07123456789','C1 ABC', ["Fatigue","Fever"]),
                    ]
         
        try:
            print(f"Loading file: {file_name}") 
            for patient in patients:
              print(patient)
            with open(file_name, 'r') as file:
                for line in file:
                    try:
                        fields = line.strip().split(",")  # Split the line by comma
                        if len(fields) != 6:  # Adjust based on the number of fields in the patient record
                            raise ValueError("Incorrect number of fields in record.")
                        
                        first_name, surname, age, mobile, postcode, symptoms = fields
                        symptoms = symptoms.split(';')  # Assuming symptoms are separated by semicolons in the file
                        patient = Patient(first_name, surname, int(age), mobile, postcode, symptoms)
                        patient_list.append(patient)
                    except ValueError as e:
                        print(f"Skipping malformed record: {line.strip()} - {e}")
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' could not be found.")
        except IOError as e:
            print(f"Error reading the file '{file_name}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        if not patient_list:
            print(f"No records were loaded from '{file_name}'.")
        else:
            print(f"Patient records loaded from '{file_name}'.")

        return patient_list






    
    def view_reports(self, doctors, patients, appointments):
        """
        Displays a submenu for viewing various reports.
        """
        while True:
            print("\n--- Reports Menu ---")
            print(" a) Total number of doctors in the system")
            print(" b) Total number of patients per doctor")
            print(" c) Total number of appointments per month per doctor")
            print(" d) Total number of patients based on illness type")
            print(" e) Exiting report Menu")

            choice = input("Select a report (a/b/c/d/e): ").strip().lower()

            if choice == 'a':
                print(f"\nTotal number of doctors in the system: {len(doctors)}")
            elif choice == 'b':
                self.view_patients_per_doctor(doctors, patients)
            elif choice == 'c':
                self.view_appointments_per_month_per_doctor(appointments, doctors)
            elif choice == 'd':
                self.view_patients_by_illness(patients)
            elif choice == 'e':
                break
            else:
                print("Invalid option. Please try again.")

    def view_patients_per_doctor(self, doctors, patients):
        import matplotlib.pyplot as plt
        patients[0].assign_doctor(doctors[0])
        patients[1].assign_doctor(doctors[1])
        patients[2].assign_doctor(doctors[0])

        doctor_patient_count = {doctor.full_name(): 0 for doctor in doctors}
        for patient in patients:
            if patient.assigned_doctor:
                doctor_patient_count[patient.assigned_doctor.full_name()] += 1

        fig, ax = plt.subplots()
        doctors_names = list(doctor_patient_count.keys())
        patient_counts = list(doctor_patient_count.values())
        ax.bar(doctors_names, patient_counts)
        ax.set_xlabel('Doctors')
        ax.set_ylabel('Number of Patients')
        ax.set_title('Total Patients per Doctor')
        plt.show()

    def view_appointments_per_month_per_doctor(self, appointments, doctors):
     from collections import defaultdict
     import datetime
     import matplotlib.pyplot as plt
    
     print("\n----- Total Appointments Per Month Per Doctor -----")
    
     appointments_by_month = defaultdict(lambda: defaultdict(int))
    
     for appointment in appointments:
        try:
            date_obj = datetime.datetime.strptime(appointment['date'], "%Y-%m-%d")
            doctor_name = appointment['doctor_name']
            month_year = date_obj.strftime("%B %Y")
            appointments_by_month[doctor_name][month_year] += 1
        except KeyError:
            continue

     for doctor_name, months in appointments_by_month.items():
        print(f"\nDoctor: {doctor_name}")
        for month_year, count in months.items():
            print(f"  {month_year}: {count} appointments")
    
     for doctor_name, months in appointments_by_month.items():
        
        months_sorted = sorted(months.keys(), key=lambda x: datetime.datetime.strptime(x, "%B %Y"))
        appointment_counts = [months[month] for month in months_sorted]

        plt.figure(figsize=(8, 5))
        plt.bar(months_sorted, appointment_counts, color='skyblue')
        plt.title(f"Appointments Per Month for Dr. {doctor_name}")
        plt.xlabel("Month")
        plt.ylabel("Number of Appointments")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()
     
    def view_patients_by_illness(self, patients):
     import matplotlib.pyplot as plt
     illness_count = {}
     for patient in patients:
        for symptom in patient.get_symptoms():
            illness_count[symptom] = illness_count.get(symptom, 0) + 1

     print("\n--- Total Patients by Illness Type ---")
     for symptom, count in illness_count.items():
        print(f"{symptom}: {count} patients")

     if illness_count:
        symptoms = list(illness_count.keys())
        counts = list(illness_count.values())
        plt.figure(figsize=(10, 6))
        plt.bar(symptoms, counts, color='skyblue', edgecolor='black')
        plt.title("Total Patients by Illness Type", fontsize=16)
        plt.xlabel("Illness Type", fontsize=12)
        plt.ylabel("Number of Patients", fontsize=12)
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.show()
     else:
        print("No data available to display.")


    

    
            