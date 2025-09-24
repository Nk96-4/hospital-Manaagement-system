
class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
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
    def get_speciality(self):
        """Gets the doctor's speciality."""
        return self.__speciality

    def set_speciality(self, new_speciality):
      self.__speciality = new_speciality


    def add_patient(self, patient):
        if patient not in self.__assigned_patients:
            self.__assigned_patients.append(patient)

    def view_assigned_patients(self):
        if not self.__assigned_patients:
            print(f"Dr. {self.full_name()} has no assigned patients.")
        else:
            print(f"\nPatients assigned to Dr. {self.full_name()}:")
            for patient in self.__assigned_patients:
                print(f"- {patient.full_name()} ({patient.age} years old)")
    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
   