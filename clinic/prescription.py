class Prescription:
    prescriptions_db = []

    def __init__(self, id: int, patient_id: int, medication: str, dosage: str):
        self.id = id
        self.patient_id = patient_id
        self.medication = medication
        self.dosage = dosage
        Prescription.prescriptions_db.append(self)

    @classmethod
    def create(cls, id: int, patient_id: int, medication: str, dosage: str):
        return cls(id, patient_id, medication, dosage)

    @classmethod
    def read(cls, id: int):
        for prescription in cls.prescriptions_db:
            if prescription.id == id:
                return prescription
        raise ValueError("Рецепт с таким ID не найден!")

    def update(self, medication: str = None, dosage: str = None):
        if medication:
            self.medication = medication
        if dosage:
            self.dosage = dosage

    @classmethod
    def delete(cls, id: int):
        prescription = cls.read(id)
        cls.prescriptions_db.remove(prescription)