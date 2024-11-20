from clinic.patient import Patient
from clinic.doctor import Doctor
from clinic.appointment import Appointment
from clinic.medical_card import MedicalCard
from clinic.department import Department
from clinic.diagnosis import Diagnosis
from clinic.prescription import Prescription
from clinic.service import Service
from clinic.invoice import Invoice

# Создаем объекты
def create_objects():
    # Создаем пациентов
    patient1 = Patient.create(1, "Иванов Иван Иванович", 30, "Москва")
    patient2 = Patient.create(2, "Петров Петр Петрович", 40, "Санкт-Петербург")

    # Создаем врачей
    doctor1 = Doctor.create(1, "Доктор Алексей Алексеевич", "Терапевт")
    doctor2 = Doctor.create(2, "Доктор Ольга Владимировна", "Хирург")

    # Создаем отделения
    department1 = Department.create(1, "Терапевтическое отделение", "1 этаж")
    department2 = Department.create(2, "Хирургическое отделение", "2 этаж")

    # Создаем диагнозы
    diagnosis1 = Diagnosis.create(1, "Острые респираторные инфекции")
    diagnosis2 = Diagnosis.create(2, "Аппендицит")

    # Создаем назначения
    prescription1 = Prescription.create(1, patient1.id, "Парацетамол", "500мг 2 раза в день")
    prescription2 = Prescription.create(2, patient2.id, "Амоксициллин", "1 капсула 3 раза в день")

    # Создаем услуги
    service1 = Service.create(1, "Прием терапевта", 1500)
    service2 = Service.create(2, "Операция", 5000)

    # Создаем счета
    invoice1 = Invoice.create(1, patient1.id, 1500)
    invoice2 = Invoice.create(2, patient2.id, 5000)

    # Создаем записи на прием
    appointment1 = Appointment.create(1, doctor1.id, patient1.id, "2024-11-20 10:00")
    appointment2 = Appointment.create(2, doctor2.id, patient2.id, "2024-11-21 11:00")

    # Создаем медицинские карты
    medical_card1 = MedicalCard.create(1, patient1.id, diagnosis1.id)
    medical_card2 = MedicalCard.create(2, patient2.id, diagnosis2.id)

# Печать всех созданных объектов
def print_objects():
    print("Пациенты:")
    for patient in Patient.patients_db:
        print(f"{patient}")

    print("\nВрачи:")
    for doctor in Doctor.doctors_db:
        print(f"{doctor}")

    print("\nОтделения:")
    for department in Department.departments_db:
        print(f"{department}")

    print("\nДиагнозы:")
    for diagnosis in Diagnosis.diagnoses_db:
        print(f"{diagnosis}")

    print("\nНазначения:")
    for prescription in Prescription.prescriptions_db:
        print(f"{prescription}")

    print("\nУслуги:")
    for service in Service.services_db:
        print(f"{service}")

    print("\nСчета:")
    for invoice in Invoice.invoices_db:
        print(f"{invoice}")

    print("\nЗаписи на прием:")
    for appointment in Appointment.appointments_db:
        print(f"{appointment}")

    print("\nМедицинские карты:")
    for medical_card in MedicalCard.medical_cards_db:
        print(f"{medical_card}")

# Обновление и удаление объектов
def update_and_delete():
    # Обновление пациента
    patient_to_update = Patient.read(1)
    patient_to_update.update(name="Иванов Иван Иванович Обновлен")

    # Удаление записи на прием
    Appointment.delete(1)

# Основная функция
if __name__ == "__main__":
    create_objects()
    print_objects()
    update_and_delete()
    print("\nПосле обновления и удаления:")
    print_objects()