class Diagnosis:
    diagnoses_db = []  # База данных диагнозов

    def __init__(self, name: str):
        self.name = name
        Diagnosis.diagnoses_db.append(self)

    @staticmethod
    def get_all_diagnoses():
        return Diagnosis.diagnoses_db