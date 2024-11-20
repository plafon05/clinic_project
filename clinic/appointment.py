class Appointment:
    appointments_db = []

    def __init__(self, id: int, doctor_id: int, patient_id: int, appointment_time: str):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.appointment_time = appointment_time
        Appointment.appointments_db.append(self)

    @classmethod
    def create(cls, id: int, doctor_id: int, patient_id: int, appointment_time: str):
        return cls(id, doctor_id, patient_id, appointment_time)

    @classmethod
    def read(cls, id: int):
        for appointment in cls.appointments_db:
            if appointment.id == id:
                return appointment
        raise ValueError("Запись с таким ID не найдена!")

    def update(self, appointment_time: str = None):
        if appointment_time:
            self.appointment_time = appointment_time

    @classmethod
    def delete(cls, id: int):
        appointment = cls.read(id)
        cls.appointments_db.remove(appointment)