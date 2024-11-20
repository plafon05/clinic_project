import json
import xml.etree.ElementTree as ET
from clinic.appointment import Appointment
from clinic.diagnosis import Diagnosis
from clinic.medical_card import MedicalCard
from clinic.recipe import Recipe
from clinic.patient import Patient


class DataManager:

    @staticmethod
    def save_to_json(filename: str, data: list):
        """Сохранение данных в файл в формате JSON."""
        try:
            with open(filename, 'w') as file:
                json.dump([obj.__dict__ for obj in data], file, indent=4)
            print(f"Данные успешно сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в JSON: {e}")

    @staticmethod
    def load_from_json(filename: str, class_type):
        """Загрузка данных из файла JSON."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                objects = [class_type(**item) for item in data]
            print(f"Данные успешно загружены из {filename}")
            return objects
        except Exception as e:
            print(f"Ошибка при загрузке из JSON: {e}")
            return []

    @staticmethod
    def save_to_xml(filename: str, data: list):
        """Сохранение данных в файл в формате XML."""
        try:
            root = ET.Element("items")
            for obj in data:
                obj_elem = ET.SubElement(root, "item")
                for key, value in obj.__dict__.items():
                    child = ET.SubElement(obj_elem, key)
                    child.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(filename)
            print(f"Данные успешно сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в XML: {e}")

    @staticmethod
    def load_from_xml(filename: str, class_type):
        """Загрузка данных из файла XML."""
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            objects = []
            for item_elem in root.findall("item"):
                item_data = {child.tag: child.text for child in item_elem}
                obj = class_type(**item_data)
                objects.append(obj)
            print(f"Данные успешно загружены из {filename}")
            return objects
        except Exception as e:
            print(f"Ошибка при загрузке из XML: {e}")
            return []

    @staticmethod
    def save_all_data():
        """Сохранение всех данных в соответствующие файлы."""
        DataManager.save_to_json('patients.json', Patient.patients_db)
        DataManager.save_to_json('appointments.json', Appointment.appointments_db)
        DataManager.save_to_json('diagnoses.json', Diagnosis.diagnoses_db)
        DataManager.save_to_json('medical_cards.json', MedicalCard.medical_cards_db)
        DataManager.save_to_json('recipes.json', Recipe.recipes_db)

    @staticmethod
    def load_all_data():
        """Загрузка всех данных из файлов."""
        Patient.patients_db = DataManager.load_from_json('patients.json', Patient)
        Appointment.appointments_db = DataManager.load_from_json('appointments.json', Appointment)
        Diagnosis.diagnoses_db = DataManager.load_from_json('diagnoses.json', Diagnosis)
        MedicalCard.medical_cards_db = DataManager.load_from_json('medical_cards.json', MedicalCard)
        Recipe.recipes_db = DataManager.load_from_json('recipes.json', Recipe)
