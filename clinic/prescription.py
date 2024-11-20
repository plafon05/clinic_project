class Prescription:
    prescriptions_db = []  # База данных рецептов

    def __init__(self, doctor, medication, patient, date):
        self.doctor = doctor
        self.medication = medication
        self.patient = patient
        self.date = date
        Prescription.prescriptions_db.append(self)

    @staticmethod
    def get_all_prescriptions():
        return Prescription.prescriptions_db