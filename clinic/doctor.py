class Doctor:
    doctors_db = []  # База данных врачей

    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty
        Doctor.doctors_db.append(self)

    @staticmethod
    def get_all_doctors():
        return Doctor.doctors_db