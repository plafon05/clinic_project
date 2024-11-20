class Invoice:
    invoices_db = []

    def __init__(self, id: int, patient_id: int, amount: float):
        self.id = id
        self.patient_id = patient_id
        self.amount = amount
        Invoice.invoices_db.append(self)

    @classmethod
    def create(cls, id: int, patient_id: int, amount: float):
        return cls(id, patient_id, amount)

    @classmethod
    def read(cls, id: int):
        for invoice in cls.invoices_db:
            if invoice.id == id:
                return invoice
        raise ValueError("Счет с таким ID не найден!")

    def update(self, amount: float = None):
        if amount:
            self.amount = amount

    @classmethod
    def delete(cls, id: int):
        invoice = cls.read(id)
        cls.invoices_db.remove(invoice)