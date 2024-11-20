from clinic.data_manager import DataManager
from clinic.patient import Patient
from clinic.appointment import Appointment
from clinic.doctor import Doctor
from clinic.diagnosis import Diagnosis

def print_objects():
    """Вывод всех пациентов."""
    for patient in Patient.get_all_patients():
        print(f"Пациент: {patient.name}, Возраст: {patient.age}")

# Загружаем данные из файлов
DataManager.load_all_data()

# Выводим всех пациентов
print_objects()

# Добавляем нового пациента
new_patient = Patient(name="John Doe", age=30)

# Сохраняем все данные
DataManager.save_all_data()