class Person:
    """Parent class for common attributes and methods shared by Doctor and Patient."""

    def __init__(self, first_name, surname):
        """
        Args:
            first_name (string): First name of the person.
            surname (string): Surname of the person.
        """
        self.__first_name = first_name
        self.__surname = surname
       

    def full_name(self):
        """Returns the person's full name."""
        return f"{self.__first_name} {self.__surname} "

    def get_first_name(self):
        """Gets the person's first name."""
        return self.__first_name

    def set_first_name(self, new_first_name):
        """Sets a new first name."""
        self.__first_name = new_first_name

    def get_surname(self):
        """Gets the person's surname."""
        return self.__surname

    def set_surname(self, new_surname):
        """Sets a new surname."""
        self.__surname = new_surname
        
    

"""sub class doctor"""
class Doctor(Person):
    """A class representing a doctor, inheriting from Person."""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): Doctor's first name.
            surname (string): Doctor's surname.
            speciality (string): Doctor's speciality.
        """
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__assigned_patients = []
        self.__patients = []

    def get_speciality(self):
        """Gets the doctor's speciality."""
        return self.__speciality

    def set_speciality(self, new_speciality):
        """Sets a new speciality for the doctor."""
        self.__speciality = new_speciality
    def add_patient(self, patient):
        """ Adds a patient to the doctor's list. """
        self.__patients.append(patient)
    def view_assigned_patients(self):
     """Displays all patients assigned to this doctor."""
     if not self.__patients:
        print(f"No patients are currently assigned to Dr. {self.full_name()}.")
     else:
        print(f"\n--- Patients Assigned to Dr. {self.full_name()} ---")
        for i, patient in enumerate(self.__patients, start=1):
            print(f"{i}. {patient}")

    def assign_patient(self, patient):
        """ Assign a patient to the doctor and link it to the doctor. """
        patient.assign_doctor(self)
        self.add_patient(patient)
        print(f"Patient {patient.full_name()} assigned to Dr. {self.full_name()}.")

    def __str__(self):
        """Returns a string representation of the doctor."""
        return f'{self.full_name():^30}|{self.__speciality:^15}'

"""sub class patient"""
class Patient(Person):
    """A class representing a patient, inheriting from Person."""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=None):
        """
        Args:
            first_name (string): Patient's first name.
            surname (string): Patient's surname.
            age (int): Patient's age.
            mobile (string): Patient's mobile number.
            postcode (string): Patient's postcode.
            symptoms (list): Patient's symptoms.
        """
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms if symptoms else []  
        self.assigned_doctor = None  
        

    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)

    def get_symptoms(self):
        return self.__symptoms

    def assign_doctor(self, doctor):
        """Assign a doctor to the patient."""
        self.assigned_doctor = doctor

    def view_assigned_doctor(self):
        """Prints the assigned doctor for the patient."""
        if self.assigned_doctor:
            print(f"Assigned Doctor: {self.assigned_doctor.full_name()}")
        else:
            print("No doctor has been assigned to this patient yet.")

    def print_symptoms(self):
        """Prints all the symptoms of the patient."""
        if not self.__symptoms:
            print("No symptoms reported.")
        else:
            print("Symptoms:")
            for i, symptom in enumerate(self.__symptoms, 1):
                print(f"{i}. {symptom}")

    def __str__(self):
        return f"{self.get_first_name()} {self.get_surname()}, Age: {self.__age}, Mobile: {self.__mobile}, Address: {self.__postcode}, Symptoms: {', '.join(self.__symptoms)}"

    def save_patients_to_file(patients, file_name="patients_record.txt"):
     """Save patient records to a text file."""
     with open(file_name, 'w') as file:
        for patient in patients:
            file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.__age},"
                           f"{patient.__mobile},{patient.__postcode},{';'.join(patient.__symptoms)}\n")
        print(f"Patient records saved to {file_name}.")
    

    def load_patients_from_file(file_name="patients_record.txt"):
     """Load patient records from a text file."""
     patient_list = []
     patients = [
                 Patient('Sara','Smith', 20, '07012345678','B1 234',["Cough", "Fever","Malaria"]),
                 Patient('Mike','Jones', 37,'07555551234','L2 2AB',  ["Headache","Fever","Cough"]),
                 Patient('Daivd','Smith', 15, '07123456789','C1 ABC', ["Fatigue","Fever"]),
                 ]
     try:
        for patient in patients:
         print(patient.get_first_name(), patient.get_surname(), patient.get_age(), patient.get_mobile(), patient.get_postcode(), patient.get_symptoms())
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    fields = line.strip().split(",")
                    if len(fields) != 6: 
                        raise ValueError("Incorrect number of fields in record.")
                    patient = Patient(*fields)  
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

    