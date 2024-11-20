class MedicalCard:
    medical_cards_db = []  # База данных медицинских карт

    def __init__(self, patient, card_number: str):
        self.patient = patient
        self.card_number = card_number
        MedicalCard.medical_cards_db.append(self)

    @staticmethod
    def get_all_medical_cards():
        return MedicalCard.medical_cards_db