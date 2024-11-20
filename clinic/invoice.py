class Invoice:
    invoices_db = []  # База данных счетов

    def __init__(self, amount: float, patient, diagnosis):
        self.amount = amount
        self.patient = patient
        self.diagnosis = diagnosis
        Invoice.invoices_db.append(self)

    @staticmethod
    def get_all_invoices():
        return Invoice.invoices_db