class Doctor:
    doctors_db = []

    def __init__(self, id: int, name: str, specialty: str):
        self.id = id
        self.name = name
        self.specialty = specialty
        Doctor.doctors_db.append(self)

    @classmethod
    def create(cls, id: int, name: str, specialty: str):
        return cls(id, name, specialty)

    @classmethod
    def read(cls, id: int):
        for doctor in cls.doctors_db:
            if doctor.id == id:
                return doctor
        raise ValueError("Доктор с таким ID не найден!")

    def update(self, name: str = None, specialty: str = None):
        if name:
            self.name = name
        if specialty:
            self.specialty = specialty

    @classmethod
    def delete(cls, id: int):
        doctor = cls.read(id)
        cls.doctors_db.remove(doctor)