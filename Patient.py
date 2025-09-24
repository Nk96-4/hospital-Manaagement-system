class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): Mobile number
            postcode (string): Postcode
            symptoms (list): List of symptoms (default is None)
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms if symptoms else []  
        self.__assigned_doctor = None
    def full_name(self):
        """Full name is first_name and surname."""
        return f"{self.__first_name} {self.__surname}"

    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def get_doctor(self):
        return self.__doctor

    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)

    def get_symptoms(self):
        """Returns the list of symptoms."""
        return self.__symptoms
    def assign_doctor(self, doctor):
         self.assigned_doctor = doctor
    def print_symptoms(self):
        """Prints all the symptoms of the patient."""
        if not self.__symptoms:
            print("No symptoms reported.")
        else:
            print("Symptoms:")
            for i, symptom in enumerate(self.__symptoms, 1):
                print(f"{i}. {symptom}")

    def view_assigned_doctor(self):
        if not self.__assigned_doctor:
            print(f"{self.full_name()} is not assigned to any doctor.")
        else:
            print(f"{self.full_name()} is assigned to Dr. {self.__assigned_doctor}.")
    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

