class Patient:
    patients_db = []  # База данных пациентов

    def __init__(self, name: str, age: int):
        if age <= 0:
            raise ValueError("Возраст пациента должен быть положительным числом.")
        self.name = name
        self.age = age
        Patient.patients_db.append(self)

    @staticmethod
    def get_all_patients():
        return Patient.patients_db

    @staticmethod
    def delete_patient(patient):
        if patient in Patient.patients_db:
            Patient.patients_db.remove(patient)
        else:
            raise ValueError("Пациент не найден.")