class MedicalCard:
    medical_cards_db = []  # Добавляем атрибут для хранения всех медицинских карт

    @classmethod
    def create(cls, card_id: int, patient_id: int, diagnosis_id: int) -> "MedicalCard":
        medical_card = cls(card_id, patient_id, diagnosis_id)
        cls.medical_cards_db.append(medical_card)  # Добавляем медицинскую карту в базу данных
        return medical_card

    @classmethod
    def read(cls, card_id: int) -> "MedicalCard":
        for medical_card in cls.medical_cards_db:
            if medical_card.get_card_id() == card_id:
                return medical_card
        return None

    @classmethod
    def update(cls, card_id: int, patient_id: int = None, diagnosis_id: int = None) -> None:
        medical_card = cls.read(card_id)
        if medical_card:
            if patient_id:
                medical_card.set_patient_id(patient_id)
            if diagnosis_id:
                medical_card.set_diagnosis_id(diagnosis_id)

    @classmethod
    def delete(cls, card_id: int) -> None:
        medical_card = cls.read(card_id)
        if medical_card:
            cls.medical_cards_db.remove(medical_card)

    # Геттеры и сеттеры
    def __init__(self, card_id: int, patient_id: int, diagnosis_id: int):
        self.card_id = card_id
        self.patient_id = patient_id
        self.diagnosis_id = diagnosis_id

    def get_card_id(self) -> int:
        return self.card_id

    def get_patient_id(self) -> int:
        return self.patient_id

    def get_diagnosis_id(self) -> int:
        return self.diagnosis_id

    def set_patient_id(self, patient_id: int) -> None:
        self.patient_id = patient_id

    def set_diagnosis_id(self, diagnosis_id: int) -> None:
        self.diagnosis_id = diagnosis_id

    def __str__(self) -> str:
        return f"MedicalCard({self.card_id}, {self.patient_id}, {self.diagnosis_id})"