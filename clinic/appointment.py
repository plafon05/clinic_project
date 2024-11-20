class Appointment:
    appointments_db = []  # База данных назначений

    def __init__(self, patient, doctor, appointment_date):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        Appointment.appointments_db.append(self)

    @staticmethod
    def get_all_appointments():
        return Appointment.appointments_db

    @staticmethod
    def delete_appointment(appointment):
        if appointment in Appointment.appointments_db:
            Appointment.appointments_db.remove(appointment)
        else:
            raise ValueError("Запись на прием не найдена.")