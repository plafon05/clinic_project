class Service:
    services_db = []

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
        Service.services_db.append(self)

    @classmethod
    def create(cls, id: int, name: str, price: float):
        return cls(id, name, price)

    @classmethod
    def read(cls, id: int):
        for service in cls.services_db:
            if service.id == id:
                return service
        raise ValueError("Услуга с таким ID не найдена!")

    def update(self, name: str = None, price: float = None):
        if name:
            self.name = name
        if price is not None:
            self.price = price

    @classmethod
    def delete(cls, id: int):
        service = cls.read(id)
        cls.services_db.remove(service)