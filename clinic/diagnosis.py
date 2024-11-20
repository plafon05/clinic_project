class Diagnosis:
    diagnoses_db = []

    def __init__(self, id: int, diagnosis: str):
        self.id = id
        self.diagnosis = diagnosis
        Diagnosis.diagnoses_db.append(self)

    @classmethod
    def create(cls, id: int, diagnosis: str):
        return cls(id, diagnosis)

    @classmethod
    def read(cls, id: int):
        for diagnosis in cls.diagnoses_db:
            if diagnosis.id == id:
                return diagnosis
        raise ValueError("Диагноз с таким ID не найден!")

    def update(self, diagnosis: str = None):
        if diagnosis:
            self.diagnosis = diagnosis

    @classmethod
    def delete(cls, id: int):
        diagnosis = cls.read(id)
        cls.diagnoses_db.remove(diagnosis)