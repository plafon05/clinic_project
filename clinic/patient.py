from typing import List

class Patient:
    patients_db = []

    def __init__(self, id: int, name: str, age: int, gender: str):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        Patient.patients_db.append(self)

    @classmethod
    def create(cls, id: int, name: str, age: int, gender: str):
        return cls(id, name, age, gender)

    @classmethod
    def read(cls, id: int):
        for patient in cls.patients_db:
            if patient.id == id:
                return patient
        raise ValueError("Пациент с таким ID не найден!")

    def update(self, name: str = None, age: int = None, gender: str = None):
        if name:
            self.name = name
        if age is not None:
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным!")
            self.age = age
        if gender:
            self.gender = gender

    @classmethod
    def delete(cls, id: int):
        patient = cls.read(id)
        cls.patients_db.remove(patient)
