class Service:
    services_db = []  # База данных услуг

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        Service.services_db.append(self)

    @staticmethod
    def get_all_services():
        return Service.services_db