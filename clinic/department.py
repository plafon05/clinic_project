class Department:
    departments_db = []

    def __init__(self, id: int, name: str, location: str):
        self.id = id
        self.name = name
        self.location = location
        Department.departments_db.append(self)

    @classmethod
    def create(cls, id: int, name: str, location: str):
        return cls(id, name, location)

    @classmethod
    def read(cls, id: int):
        for department in cls.departments_db:
            if department.id == id:
                return department
        raise ValueError("Отделение с таким ID не найдено!")

    def update(self, name: str = None, location: str = None):
        if name:
            self.name = name
        if location:
            self.location = location

    @classmethod
    def delete(cls, id: int):
        department = cls.read(id)
        cls.departments_db.remove(department)