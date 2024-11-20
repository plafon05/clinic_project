import json
import xml.etree.ElementTree as ET
from typing import List, Dict, Any
from clinic.patient import Patient
from clinic.doctor import Doctor
from clinic.appointment import Appointment
from clinic.medical_card import MedicalCard


class DataManager:
    """Класс для управления сохранением и загрузкой данных в форматах JSON и XML."""

    @staticmethod
    def save_to_json(data: List[Dict[str, Any]], file_path: str) -> None:
        """Сохраняет данные в формате JSON."""
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в JSON: {file_path}")

    @staticmethod
    def load_from_json(file_path: str) -> List[Dict[str, Any]]:
        """Загружает данные из JSON-файла."""
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        print(f"Данные успешно загружены из JSON: {file_path}")
        return data

    @staticmethod
    def save_to_xml(data: List[Dict[str, Any]], file_path: str) -> None:
        """Сохраняет данные в формате XML."""
        root = ET.Element("data")

        for item in data:
            item_element = ET.SubElement(root, "item")
            for key, value in item.items():
                sub_element = ET.SubElement(item_element, key)
                sub_element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Данные успешно сохранены в XML: {file_path}")

    @staticmethod
    def load_from_xml(file_path: str) -> List[Dict[str, Any]]:
        """Загружает данные из XML-файла."""
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for item in root.findall("item"):
            item_data = {}
            for child in item:
                item_data[child.tag] = child.text
            data.append(item_data)

        print(f"Данные успешно загружены из XML: {file_path}")
        return data